package com.rewyndr.reflectbig.activity;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.rewyndr.reflectbig.R;
import com.rewyndr.reflectbig.interfaces.EventService;
import com.rewyndr.reflectbig.model.Contacts;
import com.rewyndr.reflectbig.service.ServiceFactory;
import com.rewyndr.reflectbig.util.SwipeDetector;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class InviteEventActivity extends Activity {
    String eventId = null;
    private List<String> emails = new ArrayList<String>();
    private Context ctx = this;
    ArrayAdapter<String> adapter;
    ListView view;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_invite_event);
        Intent intent = getIntent();
        eventId = (String) intent.getSerializableExtra("eventId");
        view = (ListView) findViewById(R.id.listView);
        adapter = new ArrayAdapter<String>(this,
                android.R.layout.simple_list_item_1, emails) {
            @Override
            public View getView(int position, View convertView,
                                ViewGroup parent) {
                View view = super.getView(position, convertView, parent);
                TextView textView = (TextView) view.findViewById(android.R.id.text1);
                textView.setTextColor(Color.BLACK);
                return view;
            }
        };
        final SwipeDetector swipeDetector = new SwipeDetector();
        view.setOnTouchListener(swipeDetector);
        view.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                if (swipeDetector.swipeDetected()) {
                    emails.remove(position);
                    adapter.notifyDataSetChanged();
                }
            }
        });
        view.setLongClickable(true);
        view.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener() {
            public boolean onItemLongClick(AdapterView<?> parent, View v, final int position, long id) {
                AlertDialog.Builder alert = new AlertDialog.Builder(
                        InviteEventActivity.this);
                alert.setTitle("Alert!!");
                alert.setMessage("Are you sure to delete record");
                alert.setPositiveButton("YES", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        emails.remove(position);
                        adapter.notifyDataSetChanged();
                        dialog.dismiss();
                    }
                });
                alert.setNegativeButton("NO", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        dialog.dismiss();
                    }
                });
                alert.show();
                return true;
            }
        });
        view.setAdapter(adapter);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.invite_event, menu);
        return true;
    }

    public void fetch(View view) {
        Intent intent = new Intent(this, ContactActivity.class);
        startActivityForResult(intent, 1234);
    }

    public void addEmail(View view) {
        EditText emails = (EditText) findViewById(R.id.email_invite);
        String email = emails.getText().toString();
        if(isValidEmail(email)) {
            this.emails.add(email);
            adapter.notifyDataSetChanged();
            emails.setText("");
        } else {
            Toast.makeText(ctx, "Invalid Email ID. Please check mail id", Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    public void onActivityResult(int reqCode, int resultCode, Intent data) {
        super.onActivityResult(reqCode, resultCode, data);
        switch (reqCode) {
            case (1234):
                if (resultCode == Activity.RESULT_OK) {
                    List<Contacts> contacts = (List<Contacts>) data.getSerializableExtra("myobj");
                    for (Contacts contact : contacts) {
                        String email = contact.getEmail();
                        if (!emails.contains(email)) {
                            emails.add(email);
                            adapter.notifyDataSetChanged();
                        }
                    }
                }
                break;
        }
    }

    public void inviteEmail(View v) {
        EventService eventService = ServiceFactory.getEventServiceInstance(this);
        try {
            eventService.inviteParticipants(eventId, emails);
            Toast.makeText(ctx, "Invitations sent", Toast.LENGTH_SHORT).show();
        } catch (Exception e) {
            e.printStackTrace();
        }
        Intent intent = new Intent(this, EventsListActivity.class);
        startActivity(intent);
    }

    public static boolean isValidEmail(String email) {
        return email.matches("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})");
    }
}
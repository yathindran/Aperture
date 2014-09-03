package com.rewyndr.reflectbig.parse.impl;

import android.content.Context;

import com.parse.ParseException;
import com.parse.ParseQuery;
import com.parse.ParseUser;
import com.rewyndr.reflectbig.interfaces.EventService;
import com.rewyndr.reflectbig.model.AttendeeStatus;
import com.rewyndr.reflectbig.model.Event;
import com.rewyndr.reflectbig.model.EventStatus;
import com.rewyndr.reflectbig.parse.model.AttendeeParse;
import com.rewyndr.reflectbig.parse.model.EventParse;
import com.rewyndr.reflectbig.parse.model.FieldNames;
import com.rewyndr.reflectbig.util.DateUtils;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by Satish on 9/2/2014.
 */
public class EventServiceParse extends ParseBase implements EventService {

    private static EventServiceParse instance = null;

    protected EventServiceParse() {
        // Exists only to defeat instantiation.
    }

    public static EventServiceParse getInstance(Context context) {
        if (instance == null) {
            initParse(context);
            instance = new EventServiceParse();
        }
        return instance;
    }

    @Override
    public Map<EventStatus, List<Event>> getEvents() throws ParseException {
        Map<EventStatus, List<Event>> eventList = new HashMap<EventStatus, List<Event>>();
        List<Event> pastEvents = new ArrayList<Event>();
        List<Event> currentEvents = new ArrayList<Event>();
        List<Event> upcomingEvents = new ArrayList<Event>();
        ParseUser current = ParseUser.getCurrentUser();
        ParseQuery<AttendeeParse> query = ParseQuery.getQuery(AttendeeParse.class);
        query.whereEqualTo(FieldNames.ATTENDEE, current);
        query.include(FieldNames.ATTENDEE_EVENT);
        query.include(FieldNames.ATTENDEE_INVITED_BY);
        List<AttendeeParse> attendeeList = query.find();
        for (AttendeeParse attendee : attendeeList) {
            Event event = getEventInfo(attendee);
            switch (event.getStatus()) {
                case PAST:
                    pastEvents.add(event);
                    break;
                case CURRENT:
                    currentEvents.add(event);
                    break;
                case UPCOMING:
                    upcomingEvents.add(event);
                    break;
            }
        }
        eventList.put(EventStatus.PAST, pastEvents);
        eventList.put(EventStatus.CURRENT, currentEvents);
        eventList.put(EventStatus.UPCOMING, upcomingEvents);
        return eventList;
    }

    @Override
    public List<String> getAttendees(String eventId) throws Exception {
        List<String> attendees = new ArrayList<String>();
        ParseQuery<AttendeeParse> query = ParseQuery.getQuery(AttendeeParse.class);
        query.whereEqualTo(FieldNames.ATTENDEE_EVENT, new EventParse(eventId));
        query.whereEqualTo(FieldNames.ATTENDEE_STATUS, AttendeeStatus.ACCEPTED.toString());
        query.include(FieldNames.ATTENDEE);
        List<AttendeeParse> attendeeParseList = query.find();
        for (AttendeeParse attendee : attendeeParseList) {
            attendees.add(attendee.getAttendee().getUsername());
        }
        return attendees;
    }

    private Event getEventInfo(AttendeeParse attendee) throws ParseException {
        Event event = new Event();
        EventParse eventParse = attendee.getEvent();
        event.setEventId(eventParse.getObjectId());
        event.setEventName(eventParse.getEventName());
        event.setEventDesc(eventParse.getEventDescription());
        event.setStartDate(eventParse.getStartDateTime());
        event.setEndDate(eventParse.getEndDateTime());
        event.setLocation(eventParse.getLocation());
        event.setShortLocation(eventParse.getEventShortLocation());
        event.setStatus(DateUtils.getEventType(event.getStartDate(), event.getEndDate()));
        event.setMyStatus(getAttendeeStatus(event.getStatus(), attendee.getStatus()));
        event.setInvitedBy(attendee.getInvitedBy().getUsername());
        eventParse.getCreatedBy().fetchIfNeeded();
        event.setCreatedBy(eventParse.getCreatedBy().getUsername());
        event.setPhotosCount(eventParse.getPhotosCount());
        event.setAttendeesCount(eventParse.getAttendeesCount());
        return event;
    }

    private AttendeeStatus getAttendeeStatus(EventStatus eventStatus, String status) {
        if (status != null) {
            switch (eventStatus) {
                case CURRENT:
                case UPCOMING:
                    if ("Y".equals(status)) {
                        return AttendeeStatus.ACCEPTED;
                    } else {
                        return AttendeeStatus.DECLINED;
                    }
                case PAST:
                    if ("Y".equals(status)) {
                        return AttendeeStatus.ATTENDED;
                    } else {
                        return AttendeeStatus.MISSED;
                    }
            }
        }
        return AttendeeStatus.NOT_RESPONDED;
    }
}

import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
list = ['tfss-14956cd0-873b-4096-905b-5142c8070dda-ch10_childs-play_640.jpg',
'tfss-45fc0070-447d-4c5c-825a-4e08c7096ee0-ch10_childs-play_1024.jpg',
'tfss-883a8470-d9fd-4275-b6d6-f8c531c9921d-Ch10_daffodils_640.jpg',
'tfss-69a727ca-bfae-476c-a61b-422a106343d8-Ch10_daffodils_1024.jpg',
'tfss-2aa6cb53-019c-4295-9ff9-700e7c84b38d-ch10_hawk_640.jpg',
'tfss-2de8ecc0-e9e0-40e2-b93a-c8880f3c4759-ch10_hawk_1024.jpg',
'tfss-09316207-94d4-40a0-861d-589f4cc44cb1-ch10_hawkhandler_640.jpg',
'tfss-714241ec-f47f-49e1-9733-8c276f9290fe-ch10_hawkhandler_1024.jpg',
'tfss-04d60ac4-69f3-41c4-81ec-2331ecd76ab7-ch10_lily1_640.jpg',
'tfss-638da9bc-5dac-44f9-824d-3070c35ca856-ch10_lily1_1024.jpg',
'tfss-972e2121-41db-4fbd-a467-52e329fb0475-ch10_lily2_640.jpg',
'tfss-c9c631ef-ae0c-4680-8a88-ca81753e129c-ch10_lily2_1024.jpg',
'tfss-1bfa0c24-2d72-4295-81e5-b2cae1b9fad6-Ch10_ostridge1_640.jpg',
'tfss-6e19d35e-7105-459f-ae77-589cb195a7dc-Ch10_ostridge1_1024.jpg',
'tfss-bacefaee-e1f8-4f82-8375-36ea278fedd1-Ch10_ostridge2_640.jpg',
'tfss-cf8b858b-6d55-4ab5-a77e-118e67e84e6e-Ch10_ostridge2_1024.jpg',
'tfss-744b970c-97c8-4bba-a2b9-c3b8ccc79367-ch10_pet-graves_640.jpg',
'tfss-92189a5f-9c6a-4d24-a869-d3f4976a25fc-ch10_pet-graves_1024.jpg',
'tfss-d17cf9f7-c804-4f8f-adb5-e2c928c40341-ch10_portriat_640.jpg',
'tfss-06d95d56-bf20-4935-b34f-3bc5f7ba6ed8-ch10_portriat_1024.jpg',
'tfss-4ff0f107-1033-4826-80e5-b699ef741a25-ch10_childs-play_640.jpg',
'tfss-11e12396-2cb9-43c4-a968-ab9e3ed7c08d-ch10_childs-play_1024.jpg',
'tfss-fa06df30-886e-49d0-ad88-256186451a61-Ch10_daffodils_640.jpg',
'tfss-6f9eb99c-02a9-47c3-aa44-fd6b5ed68446-Ch10_daffodils_1024.jpg',
'tfss-4f5798b0-03d5-4a25-b602-6c64832b8483-ch10_hawk_640.jpg',
'tfss-1da77b84-ea7b-4823-9bf8-36685ec15b02-ch10_hawk_1024.jpg',
'tfss-6548254f-1d37-47e8-bfaf-faeed643fdaf-ch10_hawkhandler_640.jpg',
'tfss-35c0dc0e-d4dd-4710-90e1-55e2073cdd2d-ch10_hawkhandler_1024.jpg',
'tfss-c9eaacf8-f327-4f8d-9e4d-3d0b7266a872-ch10_lily1_640.jpg',
'tfss-a939c20c-d48d-4684-811d-bd73be616d1c-ch10_lily1_1024.jpg',
'tfss-650f2fed-def6-4315-8506-e1868ddf5aea-ch10_lily2_640.jpg',
'tfss-58ccb88c-e231-4c6a-a3b2-2d2b6d6fe6fb-ch10_lily2_1024.jpg',
'tfss-853362d4-1d07-41b8-9b4d-97b1910337e5-Ch10_ostridge1_640.jpg',
'tfss-8743eaab-7770-43ae-a85c-315365c18cca-Ch10_ostridge1_1024.jpg',
'tfss-12be6401-aaa5-46ef-be54-92013679dad0-Ch10_ostridge2_640.jpg',
'tfss-f023e504-0cae-47e1-8bcc-921cee0eeacd-Ch10_ostridge2_1024.jpg',
'tfss-dd04a0c8-90ee-4145-99bc-5531e9bfde25-ch10_pet-graves_640.jpg',
'tfss-df6c6cd0-6b51-430f-bba4-be67eb8eb897-ch10_pet-graves_1024.jpg',
'tfss-48f164fa-146d-4b12-9543-d080763caaa7-ch10_portriat_640.jpg',
'tfss-39becb8d-e876-41f5-8439-6a89eda22d71-ch10_portriat_1024.jpg',
'tfss-5cd24333-c0e1-49b9-8e61-7c26c1f148c7-ch10_sheep_640.jpg',
'tfss-74fdc3be-3012-4800-a34f-897be142422e-ch10_sheep_1024.jpg',
'tfss-89a7d44e-c881-4ccf-8056-a5f3cf9fd702-Ch10_snowboy1_640.jpg',
'tfss-5f0b0249-e399-4660-afc0-2b391c73ed24-Ch10_snowboy1_1024.jpg',
'tfss-d3f33faa-e76b-4a3a-ac4f-a95fa908233d-Ch10_snowboy2_640.jpg',
'tfss-f564c48a-42d3-4747-9707-7aaa7d931b34-Ch10_snowboy2_1024.jpg',
'tfss-8ac89a5d-3ff4-4d12-b2cc-176c6c56ab34-Ch10_table-setting_640.jpg',
'tfss-8de746d1-78b3-4cdb-902e-61f918f1f7e0-Ch10_table-setting_1024.jpg',
'tfss-d144e69e-2556-4b5a-93dc-96a9433af46f-Ch10_wedding_640.jpg',
'tfss-094df907-81b3-4706-b42e-febdb24ecb9b-Ch10_wedding_1024.jpg',
'tfss-f54ff8e5-84ad-4319-8936-497a077a88d6-ch4_bluewater1_640.jpg',
'tfss-5d1d57ce-3580-4ddf-8833-65908853f514-ch4_bluewater1_1024.jpg',
'tfss-8e64a234-e78f-4f07-8963-44b4da12e18f-ch4_caution_640.jpg',
'tfss-9cca088e-a760-4eea-b12f-b95497d8509a-ch4_caution_1024.jpg',
'tfss-4c9aef9f-8ef5-43ac-819e-a6f8a390db1d-ch4_chromatic2_640.jpg',
'tfss-e07105eb-c67b-4159-bc3c-64524da4073a-ch4_chromatic2_1024.jpg',
'tfss-740b3070-a565-4a3b-b95e-c2cbccf8e67e-ch4_church_640.jpg',
'tfss-c2787306-c521-4ef3-a545-e3d0f6353881-ch4_church_1024.jpg',
'tfss-5b763d5c-3ecd-4c5e-94d3-6e2d06b6754e-ch4_convent_640.jpg',
'tfss-2a9a26ab-e7f9-4567-8f22-0dbe441dbc77-ch4_convent_1024.jpg',
'tfss-81bff6e4-d90c-43a5-bf92-6abb752cfaab-ch4_fashion-model_640.jpg',
'tfss-159226af-c9b5-421e-b6c0-2ec5604a4d11-ch4_fashion-model_1024.jpg',
'tfss-c0902b34-f44d-46f3-ae9d-6ac69affa69e-ch4_field_crop_640.jpg',
'tfss-42b9f204-0837-48c6-be1d-d2660aae41a1-ch4_field_crop_1024.jpg',
'tfss-ab989522-8752-4bf6-a95d-a01f782baf16-ch4_fish1_640.jpg',
'tfss-fc8b0367-7676-47ad-914a-766464195df9-ch4_fish1_1024.jpg',
'tfss-f6f647ea-3f46-41c6-9fbf-73075d232365-ch4_fish2_640.jpg',
'tfss-1c415d54-bd2a-401c-9019-622a97afc59e-ch4_fish2_1024.jpg',
'tfss-2a008291-2828-46f7-864e-f36614a999c1-ch4_flare_640.jpg',
'tfss-45b5bd4a-29e1-4b8e-9415-4b8f8e8a1906-ch4_flare_1024.jpg',
'tfss-171114b7-125b-4b1c-9b3e-69f85358d8f6-ch4_glassbuilding_640.jpg',
'tfss-5e0b7ea6-00ba-4b04-9967-4d05e2128116-ch4_glassbuilding_1024.jpg',
'tfss-393943c0-755d-48ba-b68e-a2b2b821ff8c-ch4_hockey_640.jpg',
'tfss-088e9e45-a32c-46d8-93d6-6fd501b247c2-ch4_hockey_1024.jpg',
'tfss-0cb5d9a9-9068-4019-aa0c-b8129f98360a-ch4_lamp2_crop_640.jpg',
'tfss-5a351fea-6b46-4e19-8cbc-b2da555aa28f-ch4_lamp2_crop_1024.jpg',
'tfss-6978165a-20f7-4db4-9fad-9c95a8c9fbf0-ch4_leaves_640.jpg',
'tfss-10d5a479-457f-4f2e-b4c1-dc48fd8d1381-ch4_leaves_1024.jpg',
'tfss-318e6310-39f2-4dd6-bd65-fc22f07584fa-ch4_sweden_640.jpg',
'tfss-d19c1122-f87e-4579-b605-efbacf78c11b-ch4_sweden_1024.jpg',
'tfss-54e44e83-3908-4e9e-9c74-6a7687361197-ch4_tree_640.jpg',
'tfss-685b02c6-3b88-4abd-b50b-2b1c2a1290e8-ch4_tree_1024.jpg',
'tfss-438cd5be-db00-458b-8862-3decbe25c223-ch5_BodieChurch_640.jpg',
'tfss-508d1948-70df-4c3e-8b03-d5c4895065cb-ch5_BodieChurch_1024.jpg',
'tfss-98da4a84-6579-4967-904b-f2b9c4e54da3-ch5_BodieSleigh_640.jpg',
'tfss-3b3869c3-308b-4722-b0ef-a9e632a2eccb-ch5_BodieSleigh_1024.jpg',
'tfss-f3c8a0e1-b80d-4512-9722-a93d784201ba-ch5_BodieStreet_640.jpg',
'tfss-08fc37ea-df85-4253-9442-21f9b87f0411-ch5_BodieStreet_1024.jpg',
'tfss-54685e13-c44a-45bf-8017-5b5d0deec81c-ch5_Bodie_Bed_640.jpg',
'tfss-3275282b-fa90-459a-a38f-066bafe7ca41-ch5_Bodie_Bed_1024.jpg',
'tfss-bc7aafbd-c1ad-45a4-8a4c-9dc3986f8627-ch5_BW_adjustment_640.jpg',
'tfss-c8245c62-8fdc-44cb-9d64-998e524f0ed8-ch5_BW_adjustment_1024.jpg',
'tfss-31ba61a3-4674-4078-86b9-ebc9f2930b94-ch5_color_to_BW_640.jpg',
'tfss-d5487f14-a651-411b-9465-1e08b39d5172-ch5_color_to_BW_1024.jpg',
'tfss-56df0a5a-1c9a-487f-8696-2ef0aceb18bb-ch5_Curves_Intro_640.jpg',
'tfss-01631187-22ae-4b36-b22a-736625db0b7c-ch5_Curves_Intro_1024.jpg',
'tfss-9a1c8b7c-1259-4b84-a74c-b3cccb262479-ch5_glindashouse_640.jpg',
'tfss-d402b65b-b961-410f-b5a4-f6125d98bdef-ch5_glindashouse_1024.jpg',
'tfss-47d74032-18cf-40a3-9e7c-b9a70775600b-ch5_holga_DC3_640.jpg',
'tfss-bbf38301-f402-4b61-9022-bea7ef01ae36-ch5_holga_DC3_1024.jpg',
'tfss-ad53aa92-2168-4b0b-bb9f-556eecd7d989-ch5_Irregular_Toning_640.jpg',
'tfss-f400f19d-60b9-47c6-86f4-c2516484d767-ch5_Irregular_Toning_1024.jpg',
'tfss-93d04fa7-6519-4c48-b460-53a35b5ade40-ch5_keyring_640.jpg',
'tfss-d840b177-43a6-4422-9c62-a22cef85ea91-ch5_keyring_1024.jpg',
'tfss-0f5c693d-e4cc-4c0d-902b-a04554777302-ch5_life_preserver_640.jpg',
'tfss-b59f062c-cf86-4a7b-9233-974d793ccda1-ch5_life_preserver_1024.jpg',
'tfss-c8483619-38dd-4073-b583-422e00006ddf-ch5_ny_cemetery_640.jpg',
'tfss-d8ad3762-0e29-4be1-9310-18b5d323718e-ch5_ny_cemetery_1024.jpg',
'tfss-63b970b5-d054-4376-889d-d8bd7cab067a-ch5_puma-fountain_640.jpg',
'tfss-aafd5b65-32aa-400e-ac32-2d6b15bf27cb-ch5_puma-fountain_1024.jpg',
'tfss-1c3f444a-8c21-4f05-b91e-635f46a34b64-ch5_S-Curve_640.jpg',
'tfss-48353fa0-a2c4-4d53-9083-96cd2e221979-ch5_S-Curve_1024.jpg',
'tfss-de102f8e-6a6b-4b23-9514-acaad11c636d-ch5_SkyTram_640.jpg',
'tfss-c50a798e-5d75-4b73-a4e1-38dd110e03b2-ch5_SkyTram_1024.jpg',
'tfss-adb1ea7d-aa8b-434a-bf67-8930b8fd70c9-ch5_steps_640.jpg',
'tfss-cde4be5e-724a-4d72-b13c-f362c3750406-ch5_steps_1024.jpg',
'tfss-40373e7d-c36b-422f-a06c-1e5d8b562e3a-ch6-DC3_640.jpg',
'tfss-67f89ee8-c3ab-4c1e-b0b8-4b56dcc51953-ch6-DC3_1024.jpg',
'tfss-fbcb4f8d-c3fc-4082-b85d-fcd3a1b54adb-ch6_220Volts_640.jpg',
'tfss-80db5932-9773-48e8-ad45-c2da27085027-ch6_220Volts_1024.jpg',
'tfss-335975ac-a7b0-4dbb-a851-81915308a540-ch6_BelowSeaLevel_640.jpg',
'tfss-9579b252-0640-42fd-b4f7-9cfb036c4d31-ch6_BelowSeaLevel_1024.jpg',
'tfss-beaad725-63f2-4c32-b523-ae5b2fab9ebd-ch6_DeathValleyRoad_640.jpg',
'tfss-1422e819-3fa0-4e46-8f8c-5a62456ee615-ch6_DeathValleyRoad_1024.jpg',
'tfss-b5fde2fd-8a52-48bb-918c-3fd2da87b79c-ch6_HaciendaWindow_640.jpg',
'tfss-15d4d1cd-7251-4748-8d4e-7e8d6d3cea0f-ch6_HaciendaWindow_1024.jpg',
'tfss-9e5c4295-bff7-4aa9-95ab-f92367381f96-ch6_highpass_contrast_640.jpg',
'tfss-1e9264c6-2495-4a1f-bb2f-cd33bb6f2ae5-ch6_highpass_contrast_1024.jpg',
'tfss-540c7c55-d6bb-4fb2-b92e-8e3b6fbcbd2a-ch6_Lighthouse-Overall_640.jpg',
'tfss-85a6aaf9-ae89-48f6-992a-e208edd6fa15-ch6_Lighthouse-Overall_1024.jpg',
'tfss-c9cd41e2-d18d-4384-883c-faac38e5a27e-ch6_Lighthouse-Shadows_640.jpg',
'tfss-27da23d2-92ff-417f-ab3a-bc7fa997eabe-ch6_Lighthouse-Shadows_1024.jpg',
'tfss-0a2b6612-b4b7-4e16-8807-e93ca57f5288-ch6_MagicShop_640.jpg',
'tfss-1c27b2b3-cd98-46d3-8edc-1a1cc77b9bf2-ch6_MagicShop_1024.jpg',
'tfss-7c8ee4e6-e8b9-4306-9e8e-2d230b4b602f-ch6_MissingSteps_640.jpg',
'tfss-51fa8264-a722-4b36-9efc-07cb3b2832a1-ch6_MissingSteps_1024.jpg',
'tfss-1875b443-fdfc-437d-b3f7-b051aa16c429-ch6_NoVisitors_640.jpg',
'tfss-336b3c1c-91a5-4015-b84c-49532bb0a47e-ch6_NoVisitors_1024.jpg',
'tfss-12c57700-c0ba-45db-a3d6-205c2d12b2db-ch6_OldFord_640.jpg',
'tfss-cfb5e5e1-d05f-4739-946e-9af4e1ac6b2b-ch6_OldFord_1024.jpg',
'tfss-1b1e863a-dd86-4a9f-810f-d74399baa69a-ch6_portrait_640.jpg',
'tfss-cc6dc3fa-94a4-4c1b-8c51-7280e554cb01-ch6_portrait_1024.jpg',
'tfss-da36223f-2868-4be2-bfbe-a73375ff64ee-ch6_Rope-Tires_640.jpg',
'tfss-e6abc8f3-0444-417e-8694-7ee203aa78fc-ch6_Rope-Tires_1024.jpg',
'tfss-e7b9ca1d-c40f-4fcc-94f0-b92a5902305b-ch6_ShipHouse_640.jpg',
'tfss-54f85310-041c-4b15-933d-093bcbf39c6e-ch6_ShipHouse_1024.jpg',
'tfss-ad559f56-4396-49d2-af32-d7130820a253-ch6_T-Rex_640.jpg',
'tfss-88815c6c-5fa1-4625-9fb4-b3bb31ae9139-ch6_T-Rex_1024.jpg',
'tfss-0b3b8a60-6056-45ad-9534-b76b1d8601b1-ch7_BodieMine_640.jpg',
'tfss-bcf241b6-92c0-434d-bdfe-86775a173003-ch7_BodieMine_1024.jpg',
'tfss-6cc85904-e6ab-45de-bf8f-d3e80952fd9e-ch7_CarnivalControlPanel_640.jpg',
'tfss-9c64c6df-6fd4-45d2-8bd8-712356d84b6b-ch7_CarnivalControlPanel_1024.jpg',
'tfss-26c08c66-00a9-42d9-8b70-52280b537deb-ch7_CurvesExample1_640.jpg',
'tfss-34382d9d-19af-41b9-8ad5-424e8acc1a21-ch7_CurvesExample1_1024.jpg',
'tfss-b644d4e1-c4ea-421d-a522-11a52648e5c5-ch7_CurvesExample2_640.jpg',
'tfss-8d02a983-313e-41be-8245-ad2a60780e51-ch7_CurvesExample2_1024.jpg',
'tfss-6b97a3c0-33d2-4895-8628-5f66d90f4f45-ch7_CurvesEyedroppers_640.jpg',
'tfss-c24abe2e-0ca0-4f08-a1a4-af739b850299-ch7_CurvesEyedroppers_1024.jpg',
'tfss-5209797c-8486-4f46-b22d-bf2a5a55cd4d-ch7_GrayEyedropper_640.jpg',
'tfss-488cce6d-c366-4bc4-9783-06566c914319-ch7_GrayEyedropper_1024.jpg',
'tfss-f2b47f02-0b46-4732-aa14-6680dd90a437-ch7_Harbor_Hull_640.jpg',
'tfss-91b138dd-e1e1-4562-ae3c-8507544d0232-ch7_Harbor_Hull_1024.jpg',
'tfss-b3242fc7-4ae0-47cc-a3a3-4e9b1c3d5c4d-ch7_Lab-Plowing_640.jpg',
'tfss-b2ecdb21-51e9-463c-8373-9893ac8b1b17-ch7_Lab-Plowing_1024.jpg',
'tfss-6e38ba83-7e15-45b3-b40c-982d7a8b1e1d-ch7_Levels-Eyedroppers_640.jpg',
'tfss-370d4b82-a9c7-42f0-a011-edc6de6a8049-ch7_Levels-Eyedroppers_1024.jpg',
'tfss-f108b463-86b5-430b-a232-78a1029e77fd-ch7_MailboxDetail-1_640.jpg',
'tfss-10974773-3b98-4a90-8e87-2096e53394f9-ch7_MailboxDetail-1_1024.jpg',
'tfss-8a5d54a7-bb42-4664-a318-a0707ff5cd35-ch7_MailboxDetail-2_640.jpg',
'tfss-835c0c2c-9c82-444a-bda7-205d5ce75d58-ch7_MailboxDetail-2_1024.jpg',
'tfss-adefcd9c-1c9c-4b71-9e26-194902cd69ae-ch7_Manual_MidtoneFix_640.jpg',
'tfss-1decc053-7084-4b74-9933-71e55536b77e-ch7_Manual_MidtoneFix_1024.jpg',
'tfss-c7e013ef-861f-489c-a8ee-fc486f5005a8-ch7_NoNeutralGuide_640.jpg',
'tfss-9d5366d0-3730-4c95-b359-2f26e20de47c-ch7_NoNeutralGuide_1024.jpg',
'tfss-0ca42b1a-40e6-421c-ab61-09c7d712d15d-ch7_RedBoat_640.jpg',
'tfss-9f0af412-60ff-4e43-9e5e-de7f907862f5-ch7_RedBoat_1024.jpg',
'tfss-8b888222-9f09-4660-91e2-1c280ffc2406-ch7_Temple_640.jpg',
'tfss-e685220c-7494-4202-a5f0-204ef6590e29-ch7_Temple_1024.jpg',
'tfss-8719d7c9-0ddb-49d7-b829-e945c06d5fc8-ch7_violin_640.jpg',
'tfss-3a251861-889a-462f-bf49-b7d4a643fa90-ch7_violin_1024.jpg',
'tfss-7cb89068-b9fa-4f0d-8094-425b3518cc51-ch8_2girls_640.jpg',
'tfss-a486f9fa-652c-4845-a056-89f132459000-ch8_2girls_1024.jpg',
'tfss-5c5891ac-172e-4859-b1d1-c1a73c7b1dd0-ch8_birdhandler_640.jpg',
'tfss-bdc8f282-da97-482d-be8a-be724e5bf429-ch8_birdhandler_1024.jpg',
'tfss-cc643826-8f85-4259-9ec4-52e866a23fc2-ch8_cactus_640.jpg',
'tfss-612015b5-f57d-4fb2-8391-543aefab735c-ch8_cactus_1024.jpg',
'tfss-2acdb8cc-cd1d-450f-9a35-c4f05d106212-ch8_ChyslerBuilding_640.jpg',
'tfss-1fdf6cc6-4e9e-4a73-be4b-1411d3236b24-ch8_ChyslerBuilding_1024.jpg',
'tfss-ea46056c-45db-4bc2-8be3-3acdacae1af4-ch8_CrossProcess_640.jpg',
'tfss-d2c131c1-27fc-4370-99cf-269af523f779-ch8_CrossProcess_1024.jpg',
'tfss-d08d6f52-106b-42b3-8d0f-f570fbd7c2a3-ch8_door_640.jpg',
'tfss-53dac541-7e43-4a2f-adba-b69bd0384899-ch8_door_1024.jpg',
'tfss-cf550d2e-61f9-4f7e-8a4f-291a8a58c64d-ch8_Fountain_640.jpg',
'tfss-5d48e296-527b-40de-b461-511d528fa53c-ch8_Fountain_1024.jpg',
'tfss-133cf407-2c95-4de5-b39f-745f89a54b91-ch8_hawk_640.jpg',
'tfss-496d82f8-65cd-416e-a0ab-eee90a223228-ch8_hawk_1024.jpg',
'tfss-39a2ab96-e70c-4151-9f3d-5f8ad31bb4a7-ch8_Sailboats_640.jpg',
'tfss-6c2ad01a-dd0c-400d-8b95-99868f83128d-ch8_Sailboats_1024.jpg',
'tfss-f010d481-56ec-4db5-806c-22fde677c4db-ch8_statue_640.jpg',
'tfss-77e073ed-ccb7-4b2e-8675-01923f294023-ch8_statue_1024.jpg',
'tfss-4407082d-65b1-4d1c-9a17-6e49b7ae5079-ch8_worldsfair_640.jpg',
'tfss-1c8e8be6-a217-4db2-b580-4662ccbefe23-ch8_worldsfair_1024.jpg',
'tfss-bf27b493-56f7-4dbe-91e5-5d6dfa9dd7f0-ch9_BWinfrared_640.jpg',
'tfss-a61927ef-4192-4836-8a17-9a11d7288351-ch9_BWinfrared_1024.jpg',
'tfss-f9fffdfb-a3d8-42f5-baf4-e5733c7b4a7b-ch9_canvas_640.jpg',
'tfss-f6202520-61c0-4af2-badf-4620234e396c-ch9_canvas_1024.jpg',
'tfss-4d026457-a37d-419f-bda2-d8ac339c9747-ch9_DiffusionFarm_640.jpg',
'tfss-0c62cbe0-aba5-4625-b457-aced74de07ce-ch9_DiffusionFarm_1024.jpg',
'tfss-11933c88-ee13-405c-85a6-53cc8265922e-ch9_fadedcolor_640.jpg',
'tfss-c6777d8d-a7b7-47b8-ae8a-1014174e3fd2-ch9_fadedcolor_1024.jpg',
'tfss-f8ec7ce7-a988-4670-bea6-b364ed2af860-ch9_filmgrain_640.jpg',
'tfss-7b8690b9-6476-40b7-95f4-9fbce5e73d42-ch9_filmgrain_1024.jpg',
'tfss-20ae0d1b-bdfe-4601-a581-5bd256f02dab-ch9_lighthouse_640.jpg',
'tfss-7eb863fa-f531-4967-9216-f1baac41cc88-ch9_lighthouse_1024.jpg',
'tfss-e3877f41-8d6b-4bd1-8612-78c30561cb78-ch9_peelingpaint_640.jpg',
'tfss-9fac2a7e-0a71-4bb3-8e70-bfced3b7377c-ch9_peelingpaint_1024.jpg',
'tfss-9b56f810-9e67-4bdc-8bc4-a8ca1f2c24c2-ch9_queenmary2005_640.jpg',
'tfss-2f32ba94-0ff5-4c95-960e-872d558349f4-ch9_queenmary2005_1024.jpg',
'tfss-4069b1d8-5103-4216-b1a7-9c8b488d6e0b-ch9_reticulation_640.jpg',
'tfss-295ecd57-db1e-4f2a-9cf5-d3a522c5221b-ch9_reticulation_1024.jpg',
'tfss-cbe59df2-a17c-4823-9d48-d8699675ea26-ch9_sepiaesque_640.jpg',
'tfss-45633915-62e6-4ecf-b93a-539128fa298e-ch9_sepiaesque_1024.jpg',
'tfss-edda7b09-35b2-4313-aef8-789d44be5a60-ch9_solarize_640.jpg',
'tfss-b495a69e-efbc-4b2f-918a-29300ece1f93-ch9_solarize_1024.jpg',
'tfss-5cff31af-1c35-4fe6-bb3e-9ce17bf51e1e-ch9_treeroots_640.jpg',
'tfss-a49ac961-134f-4ddf-a1a1-8823fdd06a06-ch9_treeroots_1024.jpg',
'tfss-ad564afe-74d5-4931-b46b-b4082e44cdd3-ch9_vintage_photopaper_640.jpg',
'tfss-4b19397d-80ab-4894-9d15-5201580ccc75-ch9_vintage_photopaper_1024.jpg',
'tfss-b796d02b-d595-4416-a7ed-05d62b6dca2a-file0001079221497_640.jpg',
'tfss-20eca153-a2c5-4c6f-8f67-0fe1d9db07ea-file0001079221497_1024.jpg',
'tfss-17fc243c-43dc-4edb-a843-fcfb63fe46d2-file0001116000079_640.jpg',
'tfss-33512cc8-b3c6-4290-8ce8-3e92697bc027-file0001116000079_1024.jpg',
'tfss-1864c0c9-62df-4995-b0f9-4d93213055fa-file0001141038889_640.jpg',
'tfss-bf3235ff-fc44-4d84-af0b-1c2fe3af0a6d-file0001141038889_1024.jpg',
'tfss-a454340f-2b31-4933-845e-9b8237b8dcc2-file0001176452626_640.jpg',
'tfss-627067ad-5088-490f-bb59-e5726680563a-file0001176452626_1024.jpg',
'tfss-40dba0b5-856d-461f-9462-dba87a4cc519-file0001209214386_640.jpg',
'tfss-2e72c964-711b-484b-b8d3-4a1074d854b1-file0001209214386_1024.jpg',
'tfss-6bb641e8-f31a-48f2-9241-ab894611af0d-file0001224117612_640.jpg',
'tfss-f6a8b58f-cb31-4187-ab4c-702113bc6860-file0001224117612_1024.jpg',
'tfss-48cec52f-b8f2-41a0-9576-b1f8d5946bbc-file0001316404158_640.jpg',
'tfss-a37c6cb3-665c-4e9f-afbe-efa90547ee72-file0001316404158_1024.jpg',
'tfss-4c4c0001-0245-4776-b922-276f05c916b6-file000132701536_640.jpg',
'tfss-584d62dd-8c4a-43e4-9173-f7ccc1087828-file000132701536_1024.jpg',
'tfss-573603ff-0580-4a78-8b84-b8107e129949-file0001376718168_640.jpg',
'tfss-327b8687-1a7f-4fa1-96fb-53da9393cc47-file0001376718168_1024.jpg',
'tfss-5ca2b024-2d2d-482f-8070-ea1a224110de-file0001454659375_640.jpg',
'tfss-c4de72e5-f758-4e76-91be-fa6145bac1bd-file0001454659375_1024.jpg',
'tfss-4b21c2dc-c61b-4cf3-a7c6-28c213dff210-file0001545806234_640.jpg',
'tfss-b930bfa3-c4b8-4626-8d10-926efcd2eba5-file0001545806234_1024.jpg',
'tfss-5991460d-1778-4c8d-9b10-597c6eeb6727-file0001565782100_640.jpg',
'tfss-31a7174b-ecc8-4ea1-a106-fcdc2ef12b98-file0001565782100_1024.jpg',
'tfss-5a23d43b-883d-429b-8b58-7b2dae832df0-file0001601969844_640.jpg',
'tfss-84d1a78d-4344-45fb-a9dc-f85bd66ed5b5-file0001601969844_1024.jpg',
'tfss-4e1be68e-6522-4abd-ae79-4f131fc36516-file0001608482449_640.jpg',
'tfss-f2c74b8d-0af8-4d15-b951-6067466364cd-file0001608482449_1024.jpg',
'tfss-ac9cb5ea-9ba4-486c-abd8-0a6a53de7b78-file0001625591306_640.jpg',
'tfss-82ce7ee8-1321-41a8-b774-a23a22d6c639-file0001625591306_1024.jpg',
'tfss-62239af7-e1ad-45a0-a632-e88f454a265f-file0001637922945_640.jpg',
'tfss-1b5401d4-47a0-434f-925b-bd641d809e80-file0001637922945_1024.jpg',
'tfss-14aa9217-c491-46b1-aa5b-518cef834919-file0001706961259_640.jpg',
'tfss-6ee7b315-e497-4735-8dff-d3dbb7eae50c-file0001706961259_1024.jpg',
'tfss-ea9a0752-1440-472e-bb2b-c2d390beddf7-file0001735386118_640.jpg',
'tfss-da014934-86f0-4901-988f-e76a3d744ef9-file0001735386118_1024.jpg',
'tfss-dd4595e5-7200-4232-baad-d8d1bc2cddd5-file0001750264747_640.jpg',
'tfss-ecdebc23-4ab4-43f0-aded-c743f642b9a1-file0001750264747_1024.jpg',
'tfss-b41a24ec-f49e-47b0-8843-72b22a073678-file0001792779106_640.jpg',
'tfss-b37357c5-d115-4822-a259-d9b99b89aaa5-file0001792779106_1024.jpg',
'tfss-7c3804c2-1442-4ad0-b781-329fa9fe0533-file0001817248786_640.jpg',
'tfss-f13c4832-61d0-4ccf-8046-a69b84ce6891-file0001817248786_1024.jpg',
'tfss-5796bfc5-9a1b-4fd6-a3db-fcfc3dfc71b3-file0001896291699_640.jpg',
'tfss-4a7b1767-c28b-4da5-a2fb-863f5c235df1-file0001896291699_1024.jpg',
'tfss-229d5bb7-1091-43d1-bbf1-3e041ba6c80e-file0001958769599_640.jpg',
'tfss-89f425b6-61b7-4010-affc-d366175d3604-file0001958769599_1024.jpg',
'tfss-cc08b561-e9b7-433e-b344-08ad4b8c95f0-file0001966720664_640.jpg',
'tfss-8845674e-73ca-4a5d-adfa-55e37f276f95-file0001966720664_1024.jpg',
'tfss-43d2bef3-3da1-4c16-b21d-11d49479e707-file0001971407787_640.jpg',
'tfss-ce4fdf0a-c8fc-4b40-bf79-4b9dc1b130be-file0001971407787_1024.jpg',
'tfss-5af40194-d868-4c09-8c89-f2ec8fba5e02-file0002056219390_640.jpg',
'tfss-3cea820c-0d59-4dc3-a502-2c31ccaf3906-file0002056219390_1024.jpg',
'tfss-855862d4-d40d-405a-91e4-1fda63a859f3-file0002063905655_640.jpg',
'tfss-b2847ba4-79d2-4d11-9144-6c8d8bb888e7-file0002063905655_1024.jpg',
'tfss-e2255b70-7af3-4144-b63f-5d4d6ca1c3df-file0002073981867_640.jpg',
'tfss-dd9e7795-7244-4bae-9927-e65e953ed1ba-file0002073981867_1024.jpg',
'tfss-88b3212b-5910-4774-9dec-59edf6dba866-file0002081215668_640.jpg',
'tfss-834266ef-2f52-4a7e-a085-23246b764613-file0002081215668_1024.jpg',
'tfss-a5aa733e-464e-41b5-bde0-293345a9da6a-file000267747089_640.jpg',
'tfss-ce0d45ab-a839-4ea2-a0ca-0da4fdfad9f7-file000267747089_1024.jpg',
'tfss-d8011d6a-f511-476a-b3df-b9f39b004d21-file000267804564_640.jpg',
'tfss-1b673281-5129-44a6-810c-1d8b28055f59-file000267804564_1024.jpg',
'tfss-ccda345d-c430-4e58-8a17-f582cb51736a-file000325161223_640.jpg',
'tfss-303c4cfe-8eaa-4b4c-998d-6aed48e97448-file000325161223_1024.jpg',
'tfss-efb94c63-704f-4e8f-89ce-e81a71db882f-file000466623310_640.jpg',
'tfss-3afaae5e-0511-461d-b563-bfb824e6e233-file000466623310_1024.jpg',
'tfss-2b2856d3-831b-40cb-8ae2-1a52302aaac2-file000477760838_640.jpg',
'tfss-59df7507-642b-486b-90ed-a9da75fe3004-file000477760838_1024.jpg',
'tfss-ba7aaa1c-02b7-4810-9533-e72e184c6779-file00053809264_640.jpg',
'tfss-c12b79c0-f685-4ec9-849e-04f0d32001dc-file00053809264_1024.jpg',
'tfss-8da48b12-ea4c-4af6-90fc-a88e3e24d724-file000541344089_640.jpg',
'tfss-9a5e13b8-0d49-400f-b215-861e9d2aa985-file000541344089_1024.jpg',
'tfss-e07ab4fc-b0c7-47dc-b5d3-201d3588d073-file000555007525_640.jpg',
'tfss-2818621f-714f-48dd-8653-a90e63f77af3-file000555007525_1024.jpg',
'tfss-92577ae5-02e5-4319-b9ce-344a9ed009a5-file000615586116_640.jpg',
'tfss-8ec34176-f9bd-4233-bef6-4dd54ff7b790-file000615586116_1024.jpg',
'tfss-158e0d47-6bc3-4448-85c5-7f58be802013-file000626266718_640.jpg',
'tfss-94b3d6dc-febf-42be-97c7-52d1586eecdc-file000626266718_1024.jpg',
'tfss-bf63e6ec-87cb-4f02-b9dc-d2da9f1ce62f-file000656451307_640.jpg',
'tfss-3d676850-f476-400a-a684-c9122223b91e-file000656451307_1024.jpg',
'tfss-7e864736-31e7-47bf-8557-d6e67fd3c359-file000693070568_640.jpg',
'tfss-944ddafc-df3d-4fd6-99b3-fa21e6b1c23d-file000693070568_1024.jpg',
'tfss-32c0fb5a-5590-436d-8b24-bf8e823af527-file000698862236_640.jpg',
'tfss-0545477e-a59c-4b70-9cba-726154481a9a-file000698862236_1024.jpg',
'tfss-c2beb7c5-6869-42f6-ad63-7164bf20f1c9-file000738769552_640.jpg',
'tfss-0a4acbbd-319a-4f0c-bd79-6d54b262059b-file000738769552_1024.jpg',
'tfss-543c191a-634b-481a-830a-3a957b09d56d-file000741141463_640.jpg',
'tfss-34087ee4-3973-43c2-aa84-e301d35989b1-file000741141463_1024.jpg',
'tfss-d36027b2-f21d-44b5-81fd-093943a4b5e3-file000844922903_640.jpg',
'tfss-d1f751a1-26a3-4be4-8e63-0aeb30d3ed9c-file000844922903_1024.jpg',
'tfss-24bbd87b-6c5a-45e7-ac7d-3475a27f718d-file000855094214_640.jpg',
'tfss-7aea8c6c-1b89-4a1f-868b-730b4ea35cd6-file000855094214_1024.jpg',
'tfss-900e55d0-33c6-4306-a2a5-037abd3e0374-file000927030990_640.jpg',
'tfss-04a78fc6-b5be-40ac-9fae-a8241bc71e29-file000927030990_1024.jpg',
'tfss-38941cd5-5f47-4caf-b98e-2c9601c05b1a-file1301234046357_640.jpg',
'tfss-04807ab5-6ced-4f69-9862-fde3e81259ea-file1301234046357_1024.jpg',
'tfss-58ffc1c2-fed5-41cf-953b-e90beb5e1c0b-file1561246251481_640.jpg',
'tfss-b4eec275-ad8a-420d-bea6-894151ea3f23-file1561246251481_1024.jpg',
'tfss-756cdc36-c0ff-4995-9403-0c14c77c04fe-file1651272386454_640.jpg',
'tfss-da9864a1-ffa6-4f44-9eae-26f4ccae6b0d-file1651272386454_1024.jpg',
'tfss-a325a02f-13e1-428a-add7-49ed761f3896-file1821253941895_640.jpg',
'tfss-5e371013-d455-4aed-815a-9627700d0035-file1821253941895_1024.jpg',
'tfss-e7383d1a-d16b-4939-ab09-419e0b406c0e-file2231273355591_640.jpg',
'tfss-21867d38-7b88-4533-bda2-7fbc16d175e2-file2231273355591_1024.jpg',
'tfss-b1954b6c-d31f-45f2-9e62-1e475420ad23-file2961261953471_640.jpg',
'tfss-be4d640e-00c3-4514-be97-9e9e36503b5c-file2961261953471_1024.jpg',
'tfss-5ddf0025-6677-4aa7-9125-7ca212aaece5-file2961342149502_640.jpg',
'tfss-f097d4c5-8091-4a0f-a504-8edd8f941836-file2961342149502_1024.jpg',
'tfss-9816ac22-eda7-4ea7-b760-c992bda1d621-file3181278525287_640.jpg',
'tfss-939dc480-d9d0-4fea-8646-c7094883a314-file3181278525287_1024.jpg',
'tfss-25079855-294f-4a89-bf9e-306230f57143-file3251255366828_640.jpg',
'tfss-b9a5b0a8-c4be-4193-8b2c-7f5e560a39c6-file3251255366828_1024.jpg',
'tfss-17289206-09b6-43cc-9b0d-60fa59a7807a-file3811267338835_640.jpg',
'tfss-e65cea02-b14d-4970-98bc-80c4cb19ee90-file3811267338835_1024.jpg',
'tfss-d642f0ba-3a0b-4189-a977-42fda3fb8a2d-file451264266022_640.jpg',
'tfss-9b8a34f4-37d9-41e8-95e4-46aa398a7b74-file451264266022_1024.jpg',
'tfss-e0041fa8-c3c9-4201-847f-5194d7944539-file4741298583098_640.jpg',
'tfss-04d29a4c-d08c-4ac3-937c-6673c3ff869b-file4741298583098_1024.jpg',
'tfss-14c6e21f-ecff-4eb0-a51d-b77064a75253-file4811312660912_640.jpg',
'tfss-f26bd542-3739-4f62-80ae-ecb3e606edd3-file4811312660912_1024.jpg',
'tfss-c7e5c6bc-5830-409d-b3b9-002fd6b65a4c-file4821300966298_640.jpg',
'tfss-1f5ab3dc-e1ad-4924-a639-bd5b17f48122-file4821300966298_1024.jpg',
'tfss-4dbf84ae-20dc-438b-813b-2d482a6f73ef-file5001258630705_640.jpg',
'tfss-ac343371-4cfa-422b-8eae-9f99bff36740-file5001258630705_1024.jpg',
'tfss-9e6e9d1e-9d27-46c0-8bb0-e5fa0222427c-file5051300055797_640.jpg',
'tfss-989f9cdd-9f83-4ece-be69-59058c4ae375-file5051300055797_1024.jpg',
'tfss-202865f5-890a-4f99-8460-c997e7054ea2-file5391259700152_640.jpg',
'tfss-598d3bd2-5bef-4b6a-814e-0f3911cc789c-file5391259700152_1024.jpg',
'tfss-33dcd0c2-493c-4db4-ad04-9fe00ed81b4c-file5861288554715_640.jpg',
'tfss-6a284fe9-fcf0-4e46-a4c8-64c93a6b0164-file5861288554715_1024.jpg',
'tfss-026e2604-aab2-4290-96b1-11e970793d94-file621250696198_640.jpg',
'tfss-324b4d76-9761-49b4-95a6-c5ae47141b56-file621250696198_1024.jpg',
'tfss-117837ac-0517-449d-915b-0e3e473ec3dd-file7561294493011_640.jpg',
'tfss-61146508-43b6-46ce-92c9-c9930b25fefb-file7561294493011_1024.jpg',
'tfss-5d3c7df6-9b41-44b6-8e7a-a935159eb049-file761244456443_640.jpg',
'tfss-30396193-6caf-441a-9c1d-9c3c49056dbb-file761244456443_1024.jpg',
'tfss-5affa455-1b01-4d9f-85ea-4886e430cb2a-file7681334413913_640.jpg',
'tfss-472c06d7-5449-470d-b131-d2d54eb5156b-file7681334413913_1024.jpg',
'tfss-f62d2585-35db-4edf-8923-e357899c28e1-file801263247199_640.jpg',
'tfss-5ae42d4c-d18e-489b-9473-3427c111b6bd-file801263247199_1024.jpg',
'tfss-eec9ad1f-8581-438c-9530-8b1de8f547a2-file8081258144701_640.jpg',
'tfss-189420e2-90c8-4053-8686-6b3f6d673f23-file8081258144701_1024.jpg',
'tfss-d331318a-758d-4684-93e4-3c955c5ef811-file8261246814968_640.jpg',
'tfss-825f34d6-b77a-418f-a051-1c8fd8997e70-file8261246814968_1024.jpg',
'tfss-58384ea7-5218-4fa3-ab9c-fc85f79d32b1-file9221293737060_640.jpg',
'tfss-cdc610aa-ac03-4aec-b7d4-1acf4f679484-file9221293737060_1024.jpg',
'tfss-1e6af549-234e-4b14-ab1a-f791d7d743f1-file9241312063946_640.jpg',
'tfss-078f3787-b165-4e94-b21a-832876698acf-file9241312063946_1024.jpg',
'tfss-84d829fc-db9b-4481-9aad-9fec8e46d678-file991289430233_640.jpg',
'tfss-bbf6db1d-d1fa-4512-a716-8138aa270104-file991289430233_1024.jpg',
'tfss-11239f0c-5a9a-4da7-b3bd-5f56ff8da2b9-IGP2768W_640.jpg',
'tfss-18d494b0-d85d-4578-a9d3-b266a014f019-IGP2768W_1024.jpg',
'tfss-ed72356b-67c0-4899-bf0f-a471de91ab38-IMG_1533_640.jpg',
'tfss-2e559e1f-8d8d-4081-ae72-283faa75b88d-IMG_1533_1024.jpg']
for file in list:
	connection.request('DELETE', '/1/files/' + file, '', {
		   "X-Parse-Application-Id": "dUB6bvVXgV2jeEwABqDGuZs1hKUaEOtP01wfM0SN",
		   "X-Parse-Master-Key": "G4UIUZrJ0k1zk4aMNQIVtijfwpNwez9eMcYZspjj"
		 })
	result = connection.getresponse().read()
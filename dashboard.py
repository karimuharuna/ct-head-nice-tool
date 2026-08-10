import streamlit as st

st.title('CT Head Decision Support Tool')
st.caption('Based on NICE guideline NG232 (2023): Head injury — assessment and early management')

st.warning(
    "⚠️ **This is a learning/demonstration prototype, not a validated clinical device.** "
    "It must not be used to guide real patient care. Always assess patients directly, "
    "discuss with the radiology department, and follow local trust protocols per NICE guidance."
)

age_group = st.radio("Patient age", ["16 and over", "Under 16"])

st.divider()

# ---------------- ADULT PATHWAY ----------------
if age_group == "16 and over":
    st.header("Adult (16+) Assessment")

    with st.expander("Step 1: Immediate CT criteria (within 1 hour) — click to view and select"):
        gcs_12 = st.checkbox("GCS score of 12 or less on initial assessment")
        gcs_15_2hr = st.checkbox("GCS score less than 15 at 2 hours after injury")
        skull_fracture = st.checkbox("Suspected open or depressed skull fracture")
        basal_fracture = st.checkbox("Any sign of basal skull fracture (haemotympanum, panda eyes, CSF leak, Battle's sign)")
        seizure = st.checkbox("Post-traumatic seizure")
        focal_deficit = st.checkbox("Focal neurological deficit")
        vomiting = st.checkbox("More than one episode of vomiting")

    immediate_criteria = [gcs_12, gcs_15_2hr, skull_fracture, basal_fracture, seizure, focal_deficit, vomiting]
    immediate_indicated = any(immediate_criteria)

    with st.expander("Step 2: Loss of consciousness or amnesia? — click to view and select"):
        loc_or_amnesia = st.checkbox("Patient has had loss of consciousness or amnesia since the injury")

        eight_hour_indicated = False
        if loc_or_amnesia and not immediate_indicated:
            st.write("If yes, tick any that also apply:")
            age_65 = st.checkbox("Age 65 or over")
            bleeding_disorder = st.checkbox("Any current bleeding or clotting disorder")
            dangerous_mechanism = st.checkbox(
                "Dangerous mechanism of injury (pedestrian/cyclist struck by vehicle, "
                "occupant ejected from vehicle, fall from height of more than 1m or 5 stairs)"
            )
            retro_amnesia = st.checkbox("More than 30 minutes of retrograde amnesia")

            eight_hour_criteria = [age_65, bleeding_disorder, dangerous_mechanism, retro_amnesia]
            eight_hour_indicated = any(eight_hour_criteria)

    with st.expander("Step 3: Anticoagulant / antiplatelet treatment — click to view and select"):
        anticoag = st.checkbox(
            "On anticoagulant (VKA, DOAC, heparin, LMWH) or antiplatelet treatment "
            "(excluding aspirin monotherapy), with no other indication for CT above"
        )

    with st.expander("Step 4: Time since injury — click to view and select"):
        hours_since_injury = st.number_input("Hours since injury", min_value=0.0, max_value=72.0, value=1.0, step=0.5)

    st.divider()
    st.header("Recommendation")

    if immediate_indicated:
        st.error("🔴 **Immediate CT head recommended — within 1 hour.**")
        st.write("Reason: one or more high-risk criteria present on initial assessment.")
    elif eight_hour_indicated or anticoag:
        if hours_since_injury > 8:
            st.error("🔴 **CT head recommended within 1 hour of presentation** (patient presenting more than 8 hours post-injury).")
        else:
            st.warning("🟠 **CT head recommended within 8 hours of injury.**")
        if eight_hour_indicated:
            st.write("Reason: loss of consciousness/amnesia plus an additional risk factor.")
        if anticoag:
            st.write("Reason: anticoagulant/antiplatelet treatment with no other CT indication.")
    else:
        st.success("🟢 **No CT indicated based on these criteria alone.** Continue clinical assessment and use judgement — discuss with a senior colleague if any concern remains.")

# ---------------- PAEDIATRIC PATHWAY ----------------
else:
    st.header("Paediatric (Under 16) Assessment")

    with st.expander("Step 1: Immediate CT criteria (within 1 hour) — click to view and select"):
        nai = st.checkbox("Suspected non-accidental injury")
        seizure_p = st.checkbox("Post-traumatic seizure with no history of epilepsy")
        gcs_14 = st.checkbox("GCS less than 14 on initial assessment (or less than 15 if under 1 year old)")
        gcs_15_2hr_p = st.checkbox("GCS less than 15 at 2 hours after injury")
        skull_fracture_p = st.checkbox("Suspected open/depressed skull fracture or tense fontanelle")
        basal_fracture_p = st.checkbox("Any sign of basal skull fracture")
        focal_deficit_p = st.checkbox("Focal neurological deficit")
        scalp_injury = st.checkbox("Under 1 year: bruise, swelling, or laceration more than 5cm on the head")
        bleeding_disorder_p1 = st.checkbox("Any current bleeding or clotting disorder")

    immediate_criteria_p = [nai, seizure_p, gcs_14, gcs_15_2hr_p, skull_fracture_p,
                             basal_fracture_p, focal_deficit_p, scalp_injury, bleeding_disorder_p1]
    immediate_indicated_p = any(immediate_criteria_p)

    with st.expander("Step 2: Second-tier risk factors (only relevant if none of the above apply) — click to view and select"):
        loc_5min = st.checkbox("Loss of consciousness lasting more than 5 minutes (witnessed)")
        dangerous_mechanism_p = st.checkbox(
            "Dangerous mechanism of injury (high-speed RTA as pedestrian/cyclist/vehicle occupant, "
            "fall from height of more than 3m, high-speed injury from a projectile)"
        )
        amnesia_5min = st.checkbox("Amnesia (anterograde or retrograde) lasting more than 5 minutes")
        drowsiness = st.checkbox("Abnormal drowsiness")
        vomiting_3 = st.checkbox("Three or more discrete episodes of vomiting")
        bleeding_disorder_p2 = st.checkbox("Any current bleeding or clotting disorder (if not already ticked above)")

    second_tier_count = sum([loc_5min, dangerous_mechanism_p, amnesia_5min, drowsiness, vomiting_3, bleeding_disorder_p2])

    st.divider()
    st.header("Recommendation")

    if immediate_indicated_p:
        st.error("🔴 **Immediate CT head recommended — within 1 hour.**")
        st.write("Reason: one or more high-risk criteria present on initial assessment.")
    elif second_tier_count >= 2:
        st.error("🔴 **CT head recommended within 1 hour.**")
        st.write(f"Reason: {second_tier_count} second-tier risk factors present (more than one).")
    elif second_tier_count == 1:
        st.warning(
            "🟠 **Observe for a minimum of 4 hours from time of injury.** "
            "If during observation GCS drops below 15, further vomiting occurs, or a further episode "
            "of abnormal drowsiness occurs → CT head within 1 hour."
        )
    else:
        st.success("🟢 **No CT indicated based on these criteria alone.** Continue clinical assessment and use judgement — discuss with a senior colleague if any concern remains.")

st.divider()
st.caption(
    "Source: NICE guideline NG232 (2023), Head injury: assessment and early management. "
    "https://www.nice.org.uk/guidance/ng232 — This tool is for educational/portfolio purposes only."
)
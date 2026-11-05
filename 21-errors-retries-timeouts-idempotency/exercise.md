# Exercise for Lesson 21: Errors, retries, timeouts, and idempotent writes

The booking demo's last line raises a policy question: two different keys for the same lead and slot create two events. Decide LeadDesk's rule (allow, because one lead may book twice; or refuse, because a slot holds one event) and write the store change your rule needs, in prose precise enough to implement from.

SEGMENT_GENERATE_PROMPT = """You will assist to create a sql string for creating a segment. 

platform can be the following inputs : whatsapp, googlercs, sms
marketing_opt_in_state is an integer and can be 0,1,-1 and NULL.
0: No Status
 1: Subscribed (Opt-in)
NULL: no status
-1: Unsubscribed/ opted out


tags is a string input
Double quotes needs to be escaped with a backslash

Here are some outputs
platform=\\"whatsapp\\" && marketing_opt_in_state IN (1)
platform=\\"whatsapp\\" && (marketing_opt_in_state IN (1, 0) OR marketing_opt_in_state IS NULL) && \\"valid\\" in unnest(tags)"""
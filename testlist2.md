# SEND MESSAGE


fetch("https://discord.com/api/v9/channels/882680156576153676/messages", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-US",
    "authorization": "TOKEN",
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-debug-options": "bugReporterEnabled",
    "x-fingerprint": "887113735540461650.N8qVZESZ1qBn1NfkbD_MfaA56F6",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY0MC4wIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5Ni4wLjQ2NDAuMCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NzA5NywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
  },
  "referrer": "https://discord.com/channels/882680156576153671/882680156576153676",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "{\"content\":\"YOW SICK\",\"nonce\":\"88775037740178090\",\"tts\":false}",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
});

### nonce = rand(17)

---------

# EDIT/DELETE MESSAGE - TO DELETE CHANGE REQUEST METHOD FROM POST TO DELETE

fetch("https://discord.com/api/v9/channels/882680156576153676/messages/887762879179276339", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-US",
    "authorization": "TOKEN",
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-debug-options": "bugReporterEnabled",
    "x-fingerprint": "887113735540461650.N8qVZESZ1qBn1NfkbD_MfaA56F4",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY0MC4wIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5Ni4wLjQ2NDAuMCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NzA5NywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
  },
  "referrer": "https://discord.com/channels/882680156576153671/882680156576153676",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "{\"content\":\"TEST\"}",
  "method": "PATCH",
  "mode": "cors",
  "credentials": "include"
});

# RESET PASSWORD

fetch("https://discord.com/api/v9/auth/reset", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-US",
    "authorization": "undefined",
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-debug-options": "bugReporterEnabled",
    "x-fingerprint": "887819342786482217.Wzow2XS-k13kRTZdwc_Zwjj-ZIc",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDYuMDsgTmV4dXMgNSBCdWlsZC9NUkE1OE4pIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ni4wLjQ2NDAuMCBNb2JpbGUgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijk2LjAuNDY0MC4wIiwib3NfdmVyc2lvbiI6IjYuMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NzMwOSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
  },
  "referrer": "https://discord.com/reset",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "{\"token\":\"eyJpZCI6ODgyNjc5NjI5OTA1ODA1MzY0LCJlbWFpbCI6IjE0NTA3MjM1NzZAYm1ocy5lZHUuYnoifQ.YUJ3ig.wmqVntf_XZndjvtux8n9_Gssp-w\",\"password\":\"@lexgArc1a101105\"}",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
});

# TELEMETRY

fetch("https://discord.com/api/v9/science", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-US",
    "authorization": "undefined",
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-debug-options": "bugReporterEnabled",
    "x-fingerprint": "887819342786482217.Wzow2XS-k13kRTZdwc_Zwjj-ZIc",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDYuMDsgTmV4dXMgNSBCdWlsZC9NUkE1OE4pIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ni4wLjQ2NDAuMCBNb2JpbGUgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijk2LjAuNDY0MC4wIiwib3NfdmVyc2lvbiI6IjYuMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NzMwOSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
  },
  "referrer": "https://discord.com/reset",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "{\"events\":[{\"type\":\"network_action_user_reset_password\",\"properties\":{\"client_track_timestamp\":1631746937165,\"status_code\":400,\"url\":\"/auth/reset\",\"request_method\":\"post\",\"accessibility_support_enabled\":false,\"accessibility_features\":128,\"client_uuid\":\"KVCCB/0qUgx04PIsrYGx63sBAAAEAAAA\",\"client_send_timestamp\":1631746937175}}]}",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
});


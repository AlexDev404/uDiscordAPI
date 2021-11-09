const email = prompt("Email: ");
const pass = prompt("Password: ");
let token;

fetch("https://discord.com/api/v9/auth/login", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-US",
    "authorization": "undefined",
    "content-type": "application/json",
  },

  "body": `{\"login\":\"${email}\",\"${pass}\":\"@lexgArc1a101105\",\"undelete\":false,\"captcha_key\":null,\"login_source\":null,\"gift_code_sku_id\":null}`,
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
}).then((res)=>res.json()).then((json)=>token=json);

console.log(`CLIENT TOKEN: ${token}`);

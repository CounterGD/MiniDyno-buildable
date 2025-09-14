const fetch = require('node-fetch');
const API = process.env.MINIDYNO_API || "http://127.0.0.1:8000";
const TOKEN = process.env.MINIDYNO_TOKEN || "";
async function main(){
  const res = await fetch(API + "/punishments?token=" + TOKEN);
  console.log(await res.json());
}
main();

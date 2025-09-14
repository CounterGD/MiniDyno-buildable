use std::env;
use reqwest::blocking::Client;
fn main(){
    let api = env::var("MINIDYNO_API").unwrap_or("http://127.0.0.1:8000".to_string());
    let token = env::var("MINIDYNO_TOKEN").unwrap_or("".to_string());
    let client = Client::new();
    let res = client.get(&format!("{}/punishments?token={}", api, token)).send();
    println!("{:?}", res.unwrap().text().unwrap());
}

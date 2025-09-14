package main
import (
    "fmt"
    "net/http"
    "os"
    "io/ioutil"
)
func main(){
    api := os.Getenv("MINIDYNO_API")
    if api=="" { api = "http://127.0.0.1:8000" }
    token := os.Getenv("MINIDYNO_TOKEN")
    req, _ := http.NewRequest("GET", api+"/punishments?token="+token, nil)
    resp, err := http.DefaultClient.Do(req)
    if err!=nil { panic(err) }
    defer resp.Body.Close()
    b,_ := ioutil.ReadAll(resp.Body)
    fmt.Println(string(b))
}

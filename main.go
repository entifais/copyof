package main
import (
	"fmt"
	"net/http"
	"text/template"
)
func Index(rw http.ResponseWriter, r *http.Request){
		template, _ := template.ParseFiles("templates/index.html")
		template.Execute(rw,nil)
}
func cod1(rw http.ResponseWriter, r *http.Request){
		template, _ := template.ParseFiles("templates/cod1.html")
		template.Execute(rw,nil)
}
func cod2(rw http.ResponseWriter, r *http.Request){
		template, _ := template.ParseFiles("templates/cod2.html")
		template.Execute(rw,nil)
}
func cod3(rw http.ResponseWriter, r *http.Request){
		template, _ := template.ParseFiles("templates/cod3.html")
		template.Execute(rw,nil)
}
func null(rw http.ResponseWriter, r *http.Request){
		template, _ := template.ParseFiles("templates/no.html")
		template.Execute(rw,nil)
}
func main(){
	addres := "0.0.0.0:9600"
	http.HandleFunc("/",Index)
	/*
	http.HandleFunc("/",cod1)
	http.HandleFunc("/",cod2)
	http.HandleFunc("/",cod3)
	http.HandleFunc("/",null)*/
	fmt.Println("run in "+addres)
	http.ListenAndServe(addres,nil)

}
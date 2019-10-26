package main

import (
	"fmt"
	"net/http"
)

func main(){
	http.Handle("/", http.FileServer(http.Dir("./code/lambdas")))
	e := http.ListenAndServe(":8080", nil)
	fmt.Println(e)
}

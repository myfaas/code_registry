package main

import (
	"io"
	"net/http"
	"os"
)

var (
	url = "http://192.168.74.128:8080/lambda_1.py"
)

func main() {
	res, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	f, err := os.Create("lambda_1.py")
	if err != nil {
		panic(err)
	}
	io.Copy(f, res.Body)
}
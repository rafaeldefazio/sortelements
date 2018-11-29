package main

import "flag"
import "fmt"
import "strconv"
import "encoding/csv"
import "os"

var dir string = "output/heap"


func expPassosCSV(passos [][]int){
	arquivo, erro := os.Create(fmt.Sprintf("%s/heapSortPassos.csv", dir))
	checarErro("Nao foi possivel criar arquivo", erro)
	defer arquivo.Close()

	escrever := csv.NewWriter(arquivo)
	defer escrever.Flush()


	for _, valor := range passos {
	    erro := escrever.Write([]string {fmt.Sprintf("%d", valor[0]), fmt.Sprintf("%d", valor[1]), fmt.Sprintf("%d", valor[2])})
	    checarErro("Nao foi possivel escrever arquivo", erro)
}

}

func expArrayCSV(array []string){
	arquivoArray, erro := os.Create(fmt.Sprintf("%s/array.csv", dir))
	checarErro("Nao foi possivel criar arquivo", erro)
	defer arquivoArray.Close()

	escreverArray := csv.NewWriter(arquivoArray)
	defer escreverArray.Flush()


	for _, valor := range array {
	    erro := escreverArray.Write([]string{valor})
	    checarErro("Nao foi possivel escrever arquivo", erro)
}

}

func expOArrayCSV(array []int){
	arquivoOArray, erro := os.Create(fmt.Sprintf("%s/orderedArray.csv", dir))
	checarErro("Nao foi possivel criar arquivo", erro)
	defer arquivoOArray.Close()

	escreverOArray := csv.NewWriter(arquivoOArray)
	defer escreverOArray.Flush()


	for _, valor := range array {
	    erro := escreverOArray.Write([]string {fmt.Sprintf("%d", valor)})
	    checarErro("Nao foi possivel escrever arquivo", erro)
}

}

func checarErro(msg string, erro error) {
if erro != nil {
    fmt.Println(msg, erro)
}
}

func main(){
	parametros := flag.Int("tipo", 0, "seleciona tipo de ordenacao\n\tnormal (0)\n\treversa (1)")
	flag.Parse()

	if len(flag.Args()) > 0 {
		array := flag.Args()

		var err error

		arrayN := make([]int, len(array))
		
		for i := 0; i < len(array); i++ {
			if arrayN[i], err = strconv.Atoi(array[i]); err != nil {
				panic(err)
			}

		}

		if *parametros == 0{
			heapSortAZ(array, arrayN)
		} else{
			heapSortZA(array, arrayN)
		}

		
		

	} else{
		fmt.Println("Digite um array!")
	}
}
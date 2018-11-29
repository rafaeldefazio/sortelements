package main

// "tamanho" | root | elemento eliminado
var passosZA [][]int

func heapifyZA (lista []int, n int, i int) {
	// menor elemento eh root
	menor := i

	// gera nós esquerdo e direito
	e := 2*i + 1
	d := 2*i + 2



	// verifica se há filho, e se o filho é menor que root para direita
	if e < n && lista[menor] > lista[e]{
		menor = e
		passosZA = append(passosZA, []int{n, lista[i], lista[menor]})
	}

	// e esquerda
	if d < n && lista[menor] > lista[d]{
		menor = d
		passosZA = append(passosZA, []int{n, lista[i], lista[menor]})
	}


	// troca root com ultimo elemento
	if menor != i{
		lista[i], lista[menor] = lista[menor], lista[i]
		heapifyZA(lista, n, menor)

	}



}

func heapSortZA(array []string, arrayN []int){
	n := len(arrayN)

	for i := n; i > -1; i-- {
		heapifyZA(arrayN, n, i)
	}


	for i := n-1; i >= 0; i-- {
		
		arrayN[i], arrayN[0] = arrayN[0], arrayN[i]
		passosZA = append(passosZA, []int{n, arrayN[i], arrayN[0]})
		heapifyZA(arrayN, i, 0)

	}


	expArrayCSV(array)
	expOArrayCSV(arrayN)
	expPassosCSV(passosZA)


}



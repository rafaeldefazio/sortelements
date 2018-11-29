package main


var passosAZ [][]int

func heapifyAZ (lista []int, n int, i int){
	// maior elemento eh root
	maior := i

	// gera nós esquerdo e direito
	e := 2*i + 1
	d := 2*i + 2

	// verifica se há filho, e se o filho é maior que root para direita
	if e < n && lista[i] < lista[e]{
		maior = e
		passosAZ = append(passosAZ, []int{n, lista[i], lista[maior]})
	}

	// e esquerda
	if d < n && lista[maior] < lista[d]{
		maior = d
		passosAZ = append(passosAZ, []int{n, lista[i], lista[maior]})
	}

	// troca root com ultimo elemento
	if maior != i{
		// "tamanho" | root | elemento eliminado

		
		lista[i], lista[maior] = lista[maior], lista[i]
		heapifyAZ(lista, n, maior)
	}



}

func heapSortAZ(array []string, arrayN []int){
	n := len(arrayN)

	for i := n; i > -1; i-- {
		heapifyAZ(arrayN, n, i)
	}


	for i := n-1; i > 0; i-- {
		arrayN[i], arrayN[0] = arrayN[0], arrayN[i]
		passosAZ = append(passosAZ, []int{n, arrayN[i], arrayN[0]})
		heapifyAZ(arrayN, i, 0)
	}

	expArrayCSV(array)
	expOArrayCSV(arrayN)
	expPassosCSV(passosAZ)


}



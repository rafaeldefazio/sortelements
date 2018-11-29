package main


var passos [][]int

func shellSort (lista []int) {

	// recebe tamanho da lista e tamanho do "gap", sendo tamanho da lista / 2
	n := len(lista)
	gap := n/2

	// ir de n/2 ate 1
	for gap > 0{

		// percorre itens da lista
		for i := gap; i < n; i++{

			// define variavel temporaria para trocar valores
			temp := lista[i]
			j := i

			// caso item na frente seja menor que o comparado, trocar posicoes
			for gap <= j && temp < lista[j-gap]{

				

				lista[j] = lista[j-gap]

				// lista de passos
				passos = append(passos, []int{j-gap, j})

				j -= gap
			}

			// finaliza troca
			lista[j] = temp

		}

		

		// redefine tamanho do gap, enquanto maior que 0
		gap /= 2
	}


}

func sortAZ(array []string, arrayN []int){
	

	shellSort(arrayN)
	expArrayCSV(array)
	expOArrayCSV(arrayN)
	expPassosCSV(passos)


	/*
	for i := 0; i < len(passos); i++{
		fmt.Println(gaps[i], passos[i])
	} 
*/



}



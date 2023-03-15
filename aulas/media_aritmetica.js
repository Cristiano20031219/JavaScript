var nome = "Aluno"
var materia = "Programação Web"
var valores1 = 6
var valores2 = 8
var valores3 = 7
var valores4 = 5
var media_aritmetica = (valores1+valores2+valores3+valores4)/4
console.log(nome,"Sua nota final foi",media_aritmetica)
if (media_aritmetica >= 6){
    console.log("aluno aprovado na materia de",materia)
}else if (media_aritmetica< 6){
    console.log("aluno reprovado na materia de",materia)

}
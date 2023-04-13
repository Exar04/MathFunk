const express = require('express')

const ejs = require('ejs')
 
const app = express()

app.set('view engine', 'ejs')
app.listen(4000)
app.use(express.static('public'))


app.get('/', (req, res) => {
    res.render('index')
})

app.get('/EigenValuesNVectors', (req, res) => {
    res.render('EigenValuesNVectors')
})

app.get('/QuadraticEquations', (req, res) => {
    res.render('QuadraticEquations')
})

app.get('/NLPP', (req, res) => {
    res.render('NLPP')
})

app.use((req, res) => {
    res.status(404).render('404')
})
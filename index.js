const express = require("express")
const bodyParser = require("body-parser")
const mongoose = require("mongoose")
mongoose.connect("mongodb+srv://test:test@cluster0.80jod.mongodb.net/collect?retryWrites=true&w=majority")
const app = express();
app.use(bodyParser.urlencoded({extended:true}))
app.get('/',(req,res)=>{
    res.send("hello World")
})
app.listen(3000)
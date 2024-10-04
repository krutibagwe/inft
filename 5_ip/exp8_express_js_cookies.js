//Hello.js
var express = require('express');
var app = express();
const port = 5000;


app.get('/', (req, res) => {
    res.send("Hello World!")
});


app.listen(port, () =>{
    console.log("Server is ON.");
});

//GetCookie.js
const express = require('express');
const cookieParser = require('cookie-parser');
const app = express();
const port = 5000;
app.use(cookieParser());
app.get('/getC', (req,res) => {
    const userCookie = req.cookies.user;
    if(userCookie){
        res.send(`Cookie received!! user: ${userCookie}`);
    }
    else {
        res.send('No cookie found')
    }
});


app.listen(port, () =>{
    console.log("Server is ON.");
});

//SetCookie.js
const express = require('express');
const cookieP = require('cookie-parser');
const app = express();
const port = 5000;
app.use(cookieP());
app.get('/', (req,res) => {
    res.cookie('user', 'Kruti Bagwe', {maxAge:24*60*60*1000});
    res.send("Cookie is set");
});


app.listen(port, () =>{
    console.log("Server is ON.");
});

//DelCookie.js
const express = require('express');
const cookieP = require('cookie-parser');
const app = express();
const port = 5000;
app.use(cookieP());
app.get('/clearC', (req,res) => {
    res.clearCookie('user');
    res.send("Cookie is cleared");
});


app.listen(port, () =>{
    console.log("Server is ON.");
});

const { exec } = require('child_process');
const fs = require('fs');
const prompt = require('prompt-sync')({sigint: true});
const ch=parseInt(prompt("1.Read 2.Write 3.Append 4.Copy 5.Rename 6.Delete 7.HTML output Enter the number:  "));
switch(ch){
    case 1:
        fs.readFile ("page2.txt", (err, data) =>
            {
                if (err){
                    console.log("Some error");
                }
                else {
                    console.log(data.toString());
                }
            }
            );
    break;

    case 2:
        text = " i like blue colour."
        fs.writeFile ("page3.txt", text, (err) =>
        {
            if (err){
                console.log("Some error: Cannot write into file");
        }
            else{
                console.log("File created");
            }
        } );
    break;

    case 3:
        fs.appendFile("page3.txt", " i like red colour.", (err) => {
            if (err){
                console.log("Some error");
            }
            else{
                console.log("File updated");
            }
            });
    break;

    case 4:
        fs.copyFile('page2.txt', 'page2copy.txt', (err) => {
            if (err){
                console.log("Some error");
            }
            else{
                console.log("File copied");
            }
            });
    break;

    case 5:
    fs.rename('page3.txt', 'page3rename.txt', (err) => {
        if (err){
            console.log("Some error");
        }
        else{
            console.log("File renamed");
        }
        });
    break;

    case 6:
        fs.unlink('page2copy.txt', (err) =>{
            if(err){
                console.log("Some error");
            }
            else{
                console.log("File deleted");
            }
        });
    break;

    case 7:
        const filePath = 'file1.html'; 
        const openCommand = process.platform === 'win32' ? 'start' : 'open'; 
        exec(`${openCommand} ${filePath}`, (err) => {
            if (err) {
                console.log("Some error while opening the HTML file");
            } else {
                console.log("HTML file opened in browser");
            }
        });
        break;

    default:
        console.log("Invalid choice");
}

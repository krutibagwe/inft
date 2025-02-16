class Car {
    public company: string;
    protected platenumber: number;
    private colour: string;
    constructor(company: string, platenumber: number, colour: string) {
        this.company = company;
        this.platenumber = platenumber;
        this.colour = colour;
    } 
    public display(): void {
        console.log(`Company: ${this.company}, Plate number: ${this.platenumber}`);
    }
}
class Model extends Car {
    private modelname: string;
    constructor(company: string, platenumber: number, colour: string, modelname: string) {
      super(company, platenumber, colour);
        this.modelname = modelname;
    } 
    public showDetails(): void {
        console.log(`Model: ${this.modelname}`);
        console.log(`Company: ${this.company}`);
        console.log(`Plate number: ${this.platenumber}`);  
        // console.log(`Colour: ${this.colour}`); // ❌ Error (private in base class)
    } }
const model1 = new Model("Hyundai", 12345, "Red", "i20") ;
model1.display();
model1.showDetails();
// console.log(model1.platenumber); // ❌ Error (protected)
// console.log(model1.colour); // ❌ Error (private)

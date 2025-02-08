interface Mobile {
    brand: string;
    price: number;
 }
 interface MobileDetail {
    colour: string;
    storage: number;
    }
 interface SmartPhone extends Mobile, MobileDetail {
    modelNumber: number;
    }
 let smartPhone: SmartPhone = {
     brand: "Apple",
     price: 100000,
     colour: "Black",
     storage: 128,
     modelNumber: 13
 }
 console.log("Brand is : ", smartPhone.brand);
 console.log("Price is : ", smartPhone.price);
 console.log("Colour is : ", smartPhone.colour);
 console.log("Storage is : ", smartPhone.storage);
 console.log("Model Number is : ", smartPhone.modelNumber);

import 'package:flutter/material.dart';
void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Food Delivery App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Food Delivery App'),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            // Container with a Column
            Container(
              padding: EdgeInsets.all(16.0),
              color: Colors.grey[200],
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Welcome to Food Delivery App!',
                    style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
                  ),
                  SizedBox(height: 10),
                  Text(
                    'Get food delivered at your doorstep!',
                  ),
                ],
              ),
            ),

            // Row Example
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  ElevatedButton(onPressed: () {}, child: Text('Italian')),
                  ElevatedButton(onPressed: () {}, child: Text('Chinese')),
                  ElevatedButton(onPressed: () {}, child: Text('Mexican')),
                ],
              ),
            ),
            Padding(
  padding: const EdgeInsets.all(16.0),
  child: Container(
    height: 200,
    color: Colors.blue[50],
    child: ListView.builder(
      itemCount: 10,
      itemBuilder: (context, index) {
        // List of food items
        List<String> foodItems = [  'Pizza',  'Burger',  'Pasta', 'Sushi',  'Tacos',  'Salad',  'Steak', 'Noodles',  'Sandwich',  'Fries'  ];
        
        return ListTile(
          title: Text(foodItems[index]), // Display food name
        );
      },
    ),
  ),
),   
            Padding(
  padding: const EdgeInsets.all(16.0),
  child: Container(
    height: 200,
    color: Colors.orange[50],
    child: GridView.builder(
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 3, // 3 items per row
        crossAxisSpacing: 10.0, // Horizontal spacing
        mainAxisSpacing: 10.0, // Vertical spacing
      ),
      itemCount: 9, // Number of items in the grid
      itemBuilder: (context, index) {
        // List of food offers
        List<String> foodOffers = [
          '20% OFF on Pizza',
          'Buy 1 Get 1 Free on Burgers',
          '50% OFF on Pasta',
          'Free Drink with Sushi',
          'Tacos Special: 3 for 2',
          'Salad Combo at rs 100',
          'Steak - 10% OFF this week!',
          'Ice Cream - Buy 2, Get 1 Free',
          'Sandwiches - 15% OFF on your first order',
        ];
        return Container(
          color: Colors.blue[200],
          child: Center(
            child: Text(
              foodOffers[index], // Display the offer from the list
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.bold,
                color: Colors.white,
           	       ),   
   ),    
 	),
        );
      },
    ),
  ),
),

            // Table Example
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Table(
                border: TableBorder.all(),
                children: [
                  TableRow(
                    children: [
                      Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Text('Item'),
                      ),
                      Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Text('Offer'),  ),
                    ],
                  ),
                  TableRow(
                    children: [
                      Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Text('Pizza(Small)'),
                      ),
                      Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Text('Buy 1 get 1 free!'),
                      ),
                    ],
                  ),
                  TableRow(
                    children: [
                      Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Text('Burger+Fries(Med)'),
                      ),
                      Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Text('Get one Iced Coffee'),
                      ), 
         ],  
      ),  
    ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
 

import 'package:flutter/material.dart';


void main() {
  runApp(MyApp());
}


class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Navigation & Gesture',
      theme: ThemeData(
        primarySwatch: Colors.red,
      ),
      home: HomeScreen(),
    );
  }
}


class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Home Screen')),
      drawer: Drawer(
        child: ListView(
          children: [
            DrawerHeader(
              decoration: BoxDecoration(
                  color: const Color.fromARGB(255, 223, 107, 161)),
              child: Text('Navigation Drawer',
                  style: TextStyle(color: Colors.white, fontSize: 20)),
            ),
            ListTile(
              title: Text('Second Screen'),
              onTap: () {
                // Push the second screen onto the navigation stack
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => SecondScreen()),
                );
              },
            ),
          ],
        ),
      ),
      body: Center(
        child: GestureDetector(
          onTap: () {
            // Navigate to the second screen on tap
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => SecondScreen()),
            );
          },
          child: Container(
            padding: EdgeInsets.all(20),
            decoration: BoxDecoration(
                color: const Color.fromARGB(255, 223, 107, 161),
                borderRadius: BorderRadius.circular(10)),
            child: Text('Tap Me!',
                style: TextStyle(color: Colors.white, fontSize: 18)),
          ),
        ),
      ),
    );
  }
}


class SecondScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Second Screen'),
      ),
      drawer: Drawer(
        child: ListView(
          children: [
            DrawerHeader(
              decoration: BoxDecoration(
                  color: const Color.fromARGB(255, 223, 107, 161)),
              child: Text('Navigation Drawer',
                  style: TextStyle(color: Colors.white, fontSize: 20)),
            ),
            ListTile(
              title: Text('Go Back to First Screen'),
              onTap: () {
                // Pop all screens until the HomeScreen is at the top of the stack
                Navigator.popUntil(context, ModalRoute.withName('/'));
              },
            ),
          ],
        ),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            // Pop the current screen to return to the first screen
            Navigator.pop(context);
          },
          style: ElevatedButton.styleFrom(
            backgroundColor: const Color.fromARGB(255, 223, 107, 161),
            padding: EdgeInsets.symmetric(horizontal: 40, vertical: 15),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(10),
            ),
            shadowColor: Colors.black,
            elevation: 5,
          ),
          child: Text('Go Back to First Screen',
              style: TextStyle(
                  color: Colors.white,
                  fontSize: 18,
                  fontWeight: FontWeight.bold)),
        ),
      ),
    );
  }
}

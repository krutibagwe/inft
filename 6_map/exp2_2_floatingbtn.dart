//post experiement
import 'package:flutter/material.dart';

class Counter extends StatefulWidget {
  const Counter({super.key});


  @override
  State<Counter> createState() => _CounterState();
}


class _CounterState extends State<Counter> {
  int _counter = 0;


  void _increment() {
    setState(() {
      _counter++;
    });
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: PreferredSize(
        preferredSize: const Size.fromHeight(80.0), // Increase AppBar height
        child: AppBar(
          title: const Text(
            'Kruti & Sanika',
            style: TextStyle(
              fontSize: 24,
              fontWeight: FontWeight.bold,
            ),
          ),
          backgroundColor: const Color.fromARGB(255, 152, 255, 68),
          bottom: PreferredSize(
            preferredSize: const Size.fromHeight(4.0), // Add space for the line
            child: Container(
              height: 4.0, // Line height
              color: Colors.black, // Line color
            ),
          ),
        ),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'Count: $_counter',
              style: TextStyle(
                fontSize: 30,
                fontWeight: FontWeight.bold,
                color: Colors.blue,
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _increment,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}

void main() {
  runApp(
    const MaterialApp(
      home: Counter(),
    ),
  );
}

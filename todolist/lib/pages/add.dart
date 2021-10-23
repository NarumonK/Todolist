import 'package:flutter/material.dart';

import 'package:http/http.dart' as http;
import 'dart:async';

class AddPage extends StatefulWidget {
  const AddPage({Key? key}) : super(key: key);

  @override
  _AddPageState createState() => _AddPageState();
}

class _AddPageState extends State<AddPage> {
  // ignore: non_constant_identifier_names
  TextEditingController todo_title = TextEditingController();
  TextEditingController todo_detail = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('เพิ่มรายการใหม่'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: ListView(
          children: [
            // ช่องกรอกข้อมูล title
            TextField(
                controller: todo_title,
                decoration: InputDecoration(
                    labelText: 'รายการที่ต้องทำ',
                    border: OutlineInputBorder())),
            SizedBox(
              height: 30,
            ),
            TextField(
                minLines: 4,
                maxLines: 8,
                controller: todo_detail,
                decoration: InputDecoration(
                    labelText: 'รายละเอียด', border: OutlineInputBorder())),
            SizedBox(
              height: 30,
            ),
            Padding(
              padding: const EdgeInsets.all(20),
              child: ElevatedButton(
                onPressed: () {
                  print('----------');
                  print('title: ${todo_title.text}');
                  print('title: ${todo_detail.text}');
                  postTodo();
                  setState(() {
                    todo_title.clear();
                    todo_detail.clear();
                  });
                },
                child: Text("เพิ่มรายการ"),
                style: ButtonStyle(
                    backgroundColor: MaterialStateProperty.all(Colors.blue),
                    padding: MaterialStateProperty.all(
                        EdgeInsets.fromLTRB(50, 20, 50, 20)),
                    textStyle:
                        MaterialStateProperty.all(TextStyle(fontSize: 25))),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Future postTodo() async {
    // var url = Uri.https('3575-2403-6200-8967-6332-5c38-12fb-1d37-403e.ngrok.io',
    //     '/api/post-todolist');
    // var url = Uri.http('192.168.1.182:8000', '/api/post-todolist');
    var url = Uri.http('192.168.0.110:8000', '/api/post-todolist');
    Map<String, String> header = {"Content-type": "application/json"};
    String jsondata =
        '{"title":"${todo_title.text}", "detail":"${todo_detail.text}"}';
    var response = await http.post(url, headers: header, body: jsondata);
    print('-----response-----');
    print(response.body);
  }
}

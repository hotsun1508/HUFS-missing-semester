import axios from "axios";

const putData = {
    "id": 5,
    "content": "Dart",
    "completed": true
}

axios.put('http://localhost:8001/todos/5', putData)
    .then((response) => {
        console.log(response.data)
    })
    .catch((error) => {
        console.log(error)
    })
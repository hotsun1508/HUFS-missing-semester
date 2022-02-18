import axios from "axios";

const putData = {
    "id": 5,
    "content": "Dart",
    "completed": true
}

axios({
    url: 'http://localhost:8001/todos/5',
    method: 'PUT',
    data: putData
})
    .then(response => {
        console.log(response.data)
    })
    .catch((err) => console.log(err));
import axios from "axios";

const postData = {
    "id": 5,
    "content": "R",
    "completed": false
};


axios.post('http://localhost:8001/todos', postData)
    .then((response)=> {
        console.log(response.data)
    })
    .catch((error)=> {
        console.log(error)
    })
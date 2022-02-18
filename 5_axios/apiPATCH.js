import axios from "axios";

const patchData = {
    "content": "Julia"
}

axios.patch('http://localhost:8001/todos/a5', patchData)
    .then((response) => {
        console.log(response.data)
    })
    .catch((error) => {
        console.log(error)
    })
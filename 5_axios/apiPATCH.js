import axios from "axios";

const patchData = {
    "content": "Julia"
}

axios({
    url: 'http://localhost:8001/todos/5',
    method: 'PUT',
    data: patchData
})
    .then(response => {
        console.log(response.data)
    })
    .catch((err) => console.log(err));
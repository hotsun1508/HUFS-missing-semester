const api = {
    key: "648997643def8615636111326d4ef8a1",
    baseurl: "https://api.openweathermap.org/data/2.5",
};

const searchInput = document.querySelector(".search-input");
searchInput.addEventListener("keypress", setQuery);

function setQuery(e) {
    if (e.keyCode == 13) {
        getResults(searchInput.value);
        //console.log(searchInput.value);
    }
}
// api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=648997643def8615636111326d4ef8a1
function getResults(query) {
    axios
        .get(`${api.baseurl}/weather?q=${query}&APPID=${api.key}&units=metric`)
        .then((weather) => displayResults(weather.data))
        .catch((err) => showError(query));
}

function displayResults(weather) {
    //console.log(weather);
    let city = document.querySelector(".location .city");
    city.innerText = `${weather.name}, ${weather.sys.country}`;

    let now = new Date();
    let date = document.querySelector(".location .date");
    date.innerText = dateBuilder(now);
    //console.log(now.getMonth());

    let temp = document.querySelector(".current .temp");
    temp.innerHTML = `${Math.round(weather.main.temp)} <span>°c<span>`;

    let weather_el = document.querySelector(".current .weather");
    weather_el.innerText = weather.weather[0].main;

    let hilow = document.querySelector(".current .hi-low");
    hilow.innerText = `${Math.round(weather.main.temp_min)} °c / ${Math.round(
        weather.main.temp_max
    )}°c`;
}

function dateBuilder(d) {
    let months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ];
    let days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ];

    let day = days[d.getDay()];
    let date = d.getDate();
    let month = months[d.getMonth()];
    let year = d.getFullYear();

    return `${day} ${date} ${month} ${year}`;
}

function showError(err) {
    Swal.fire({
        icon: "error",
        title: "Oops...",
        text: `${err} is not a city`,
    });
}
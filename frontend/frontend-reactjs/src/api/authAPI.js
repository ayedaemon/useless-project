export async function Signin(email, password) {
  // console.log(process.env.REACT_APP_API_PATH);
  try {
    await fetch(`${process.env.REACT_APP_API_PATH}/login`, {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify({
        email: email,
        password: password,
      }),
    })
      .then((response) => response.json())
      .then((data) => console.log(data));
  } catch (err) {
    console.log(err);
  }
}

export async function Register(username, email, password) {
  await fetch(`${process.env.REACT_APP_API_PATH}/signup`, {
    method: "POST",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify({
      username: username,
      email: email,
      password: password,
    }),
  })
    .then((response) => response.json())
    .then((data) => console.log(data));
}

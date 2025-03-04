export default async function apiFetch(
  endpoint, 
  { method, headers, body } = {}
) {
  // Verifica que la URL base sea correcta
  const BASE_URI = "http://127.0.0.1:5000/api/";
  const token = "EJiJsa3X25gDSNCPZDNfSPsq"; // Se recomienda manejar el token de manera segura

  if (token) {
    headers = {
      Authorization: `Token token=${token}`,
      ...headers,
    };
  }

  if (body) {
    headers = {
      "Content-Type": "application/json",
      ...headers,
    };
  }

  const config = {
    method: method || (body ? "POST" : "GET"),
    headers,
    body: body ? JSON.stringify(body) : null,
  };

  const response = await fetch(`${BASE_URI}${endpoint}/`, config);

  let data;
  if (!response.ok) {
    try {
      data = await response.json();
    } catch (error) {
      throw new Error(response.statusText);
    }
    throw new Error(data.errors || 'Something went wrong');
  }

  try {
    data = await response.json();
  } catch (error) {
    data = response.statusText;
  }

  return data;
}

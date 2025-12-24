const API_URL = "http://localhost:8000/query";

export async function postQuery(
  question: string,
  k: number,
  strict: boolean
) {
  const res = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      question,
      k,
      strict,
    }),
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || "API error");
  }

  return res.json();
}

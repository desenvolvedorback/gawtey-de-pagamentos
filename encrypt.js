async function getPublicKey() {
    const res = await fetch('/api/admin/public_key');
    const jwk = await res.json();
    // import key
    return await crypto.subtle.importKey(
        "jwk",
        jwk,
        { name: "RSA-OAEP", hash: "SHA-256" },
        true,
        ["encrypt"]
    );
}

async function encryptCardData(cardData) {
    const key = await getPublicKey();
    const encoder = new TextEncoder();
    const data = encoder.encode(JSON.stringify(cardData));
    const encrypted = await crypto.subtle.encrypt({ name: "RSA-OAEP" }, key, data);
    return btoa(String.fromCharCode(...new Uint8Array(encrypted)));
}
export { encryptCardData };
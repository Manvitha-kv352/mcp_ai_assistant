const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || ''
const buildUrl = (path) => API_BASE_URL ? `${API_BASE_URL.replace(/\/$/, '')}${path}` : path

export async function sendMessage(message, sessionId) {
  const response = await fetch(buildUrl('/chat'), {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message, session_id: sessionId }),
  })

  if (!response.ok) {
    const errorText = await response.text().catch(() => '')
    throw new Error(errorText || `Request failed with ${response.status}`)
  }

  const contentType = response.headers.get('content-type') || ''
  if (contentType.includes('application/json')) {
    return response.json()
  }

  return response.text()
}

export async function uploadFile(file, sessionId) {
  const formData = new FormData()
  formData.append('file', file)
  if (sessionId) {
    formData.append('session_id', sessionId)
  }

  const url = buildUrl('/upload')
  console.log('uploadFile request', { url, method: 'POST', fileName: file.name, sessionId })

  const response = await fetch(url, {
    method: 'POST',
    body: formData,
  })

  if (!response.ok) {
    const contentType = response.headers.get('content-type') || ''
    let errorText = ''

    if (contentType.includes('application/json')) {
      const payload = await response.json().catch(() => null)
      errorText = payload?.detail || payload?.message || await response.text().catch(() => '')
    } else {
      errorText = await response.text().catch(() => '')
    }

    throw new Error(errorText || `Upload failed with ${response.status}`)
  }

  return response.json()
}

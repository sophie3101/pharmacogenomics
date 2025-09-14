'use server';

import fs from 'fs/promises';
import path from 'path';

export async function uploadFile(formData: FormData) {
  const file = formData.get('file') as File;

  if (!file) {
    console.error('No file received');
    return { error: 'No file uploaded' };
  }

  try {
    const buffer = Buffer.from(await file.arrayBuffer());
    const uploadDir = path.join(process.cwd(), 'public', 'uploads');
    const filePath = path.join(uploadDir, file.name);

    await fs.mkdir(uploadDir, { recursive: true });
    await fs.writeFile(filePath, buffer);

    console.log('✅ File saved to:', filePath);

    return { message: 'File uploaded successfully!' };
  } catch (err) {
    console.error('❌ Failed to save file:', err);
    return { error: 'Upload failed' };
  }
}


'use client';
import path from 'path';
import { useState , useRef} from 'react';
import { runPharmCat } from '@/components/actions/pharmcat';
import { FormEvent } from 'react';

export default function HomePage() {
  const fileInput = useRef<HTMLInputElement>(null);
  const [status, setStatus] = useState('');
  const [showHtml, setShowHtml] = useState(false);
  const [htmlFile, setHtmlFile] = useState('');

  async function onSubmitFile(event: FormEvent<HTMLFormElement>) {
    event.preventDefault(); // prevent native submit/reload

    if (!fileInput.current?.files?.length) {
      alert('Please select a file');
      return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.current.files[0]);

    const res = await fetch('/api/upload', { 
      method: 'POST',
      body: formData,
    });

    const result = await res.json();

    // console.log(result);
    if (result.success){
      const pharmat_result = await runPharmCat(`${result.upload_dir}/${result.name}`);
      setStatus(`${pharmat_result.message}`);
      if (pharmat_result.success){
        const dirName = path.basename(result.upload_dir);
        setHtmlFile(`${dirName}/pharmcat.example.report.html`);
        setShowHtml(true);
        
        // console.log(htmlFile);
      }
    }
  }
  
  return (
    <main>
      <h1>Upload a File</h1>
      <form onSubmit={onSubmitFile}   encType="multipart/form-data">
        <input type="file" name="file" ref={fileInput}  />
        <button type="submit">RunPharmcat</button>
      </form>
      <div>
        {status && <p>{status}</p>}
        {showHtml && (
        <iframe
            src={htmlFile}
            width="100%"
            height="600px"
            style={{ border: '1px solid #ccc', marginTop: '1rem' }}
          />
        )}
      </div>
    </main>
  );
  
}

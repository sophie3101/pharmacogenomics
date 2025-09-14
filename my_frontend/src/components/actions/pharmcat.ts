'use server'
import { exec } from 'node:child_process';

const execPromise = (command: string) => {
  return new Promise((resolve, reject) => {
    exec(command, (error, stdout, stderr) => {
      if (error) {
        console.error(`exec error: ${error}`);
        return reject(error);
      }
      resolve(stdout || stderr);
    });
  });
};

export async function runPharmCat(fileName:string) {
  console.log('Running local tool...');

  try {
    // Replace 'your-local-tool-command' with the actual command.
    // Ensure the tool is accessible in the server's PATH or provide a full path.
    const output = await execPromise(`bash src/components/actions/run_pharmcat.sh ${fileName}`);
    // console.log(`Tool output: ${output}`);
    return { success: true, message: `Tool executed successfully. Output: ${output}` };
  } catch (error) {
    console.error('Failed to run tool:', error);
    return { success: false, message: `Failed to run tool. Error: ${error.message}` };
  }
}

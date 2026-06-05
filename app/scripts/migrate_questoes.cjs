const fs = require('fs');
const path = require('path');

const htmlContent = fs.readFileSync(path.join(__dirname, '../../source/questoes.html'), 'utf-8');

const match = htmlContent.match(/const allQuestions = (\{[\s\S]*?\]\n\s*\});\s*document\.addEventListener/);

if (!match) {
    // try another regex if document.addEventListener is not immediately after
    console.error("Could not find allQuestions object.");
    // let's try broader match
}

let arrayString = match ? match[1] : null;

if (!arrayString) {
    const broaderMatch = htmlContent.match(/const allQuestions = (\{[\s\S]*?\});\s*(?:const|let|var|document)/);
    if (broaderMatch) {
        arrayString = broaderMatch[1];
    }
}

if (!arrayString) {
    console.error("Failed completely to find allQuestions.");
    process.exit(1);
}

let allQuestions;
try {
    eval("allQuestions = " + arrayString);
} catch (e) {
    console.error("Error evaluating object:", e);
    process.exit(1);
}

const outputDir = path.join(__dirname, '../src/content/exercicios/questoes');
if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

function slugify(text) {
    return text.toString().toLowerCase()
        .replace(/\s+/g, '-')
        .replace(/[^\w\-]+/g, '')
        .replace(/\-\-+/g, '-')
        .replace(/^-+/, '')
        .replace(/-+$/, '');
}

let totalMigrated = 0;

for (const group of Object.keys(allQuestions)) {
    const questions = allQuestions[group];
    
    questions.forEach(q => {
        const id = `q${String(q.id).padStart(2, '0')}-${group}-${slugify(q.title)}`;
        const filename = path.join(outputDir, `${id}.md`);
        
        // Ensure properties exist
        const statementText = q.statement || "";
        let statement = statementText.replace(/\\\(/g, '$').replace(/\\\)/g, '$');
        statement = statement.replace(/\\\[/g, '$$$').replace(/\\\]/g, '$$$');
        statement = statement.replace(/<br\s*\/?>/gi, '\n\n');
        
        let solutionHtml = typeof q.resolution === 'function' ? q.resolution() : (q.resolution || "");
        let solution = solutionHtml.replace(/\\\(/g, '$').replace(/\\\)/g, '$');
        solution = solution.replace(/\\\[/g, '$$$').replace(/\\\]/g, '$$$');
        
        // Basic HTML to Markdown conversion for the solution
        solution = solution.replace(/<h[34].*?>(.*?)<\/h[34]>/g, '\n## $1\n');
        solution = solution.replace(/<p.*?>(.*?)<\/p>/g, '\n$1\n');
        solution = solution.replace(/<b.*?>(.*?)<\/b>/g, '**$1**');
        solution = solution.replace(/<strong.*?>(.*?)<\/strong>/g, '**$1**');
        // Handle step divs
        solution = solution.replace(/<div class="step">/g, '\n');
        solution = solution.replace(/<\/div>/g, '\n');
        solution = solution.replace(/<div.*?>/g, '\n');
        
        // remove extra tags
        solution = solution.replace(/<canvas.*?>.*?<\/canvas>/g, '');
        solution = solution.replace(/<ul.*?>/g, '\n');
        solution = solution.replace(/<\/ul>/g, '\n');
        solution = solution.replace(/<li.*?>/g, '- ');
        solution = solution.replace(/<\/li>/g, '\n');
        
        const markdown = `---
id: "questoes-${id}"
titulo: "${(q.title || "").replace(/"/g, '\\"')}"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "${group}"
solucao_verificada: false
---

## Enunciado

${statement}

## Solução

${solution.trim()}
`;

        fs.writeFileSync(filename, markdown);
        console.log(`Created ${id}.md`);
        totalMigrated++;
    });
}

console.log(`Migrated ${totalMigrated} questions.`);

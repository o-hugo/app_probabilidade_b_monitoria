const fs = require('fs');
const path = require('path');

const htmlContent = fs.readFileSync(path.join(__dirname, '../../source/lista_02.html'), 'utf-8');

const match = htmlContent.match(/const allQuestions = (\[[\s\S]*?\]);\s*document\.addEventListener/);

if (!match) {
    console.error("Could not find allQuestions array.");
    process.exit(1);
}

const arrayString = match[1];

let allQuestions;
try {
    eval("allQuestions = " + arrayString);
} catch (e) {
    console.error("Error evaluating array:", e);
    process.exit(1);
}

const outputDir = path.join(__dirname, '../src/content/exercicios/lista-02');
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

allQuestions.forEach(q => {
    // We already migrated q01 in a previous step, but let's overwrite or skip.
    const id = `q${String(q.id).padStart(2, '0')}-${slugify(q.title)}`;
    const filename = path.join(outputDir, `${id}.md`);
    
    // Replace \( \) with $ $ and \[ \] with $$ $$ in statement and solution
    let statement = q.statement.replace(/\\\(/g, '$').replace(/\\\)/g, '$');
    statement = statement.replace(/\\\[/g, '$$$').replace(/\\\]/g, '$$$');
    statement = statement.replace(/<br\s*\/?>/gi, '\n\n');
    
    let solutionHtml = q.solution();
    let solution = solutionHtml.replace(/\\\(/g, '$').replace(/\\\)/g, '$');
    solution = solution.replace(/\\\[/g, '$$$').replace(/\\\]/g, '$$$');
    
    // Basic HTML to Markdown conversion for the solution
    solution = solution.replace(/<h4>(.*?)<\/h4>/g, '\n## $1\n');
    solution = solution.replace(/<p>(.*?)<\/p>/g, '\n$1\n');
    solution = solution.replace(/<b>(.*?)<\/b>/g, '**$1**');
    solution = solution.replace(/<strong>(.*?)<\/strong>/g, '**$1**');
    
    const markdown = `---
id: "lista02-${id}"
titulo: "${q.title.replace(/"/g, '\\"')}"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

${statement}

## Solução

${solution.trim()}
`;

    fs.writeFileSync(filename, markdown);
    console.log(`Created ${id}.md`);
});

console.log(`Migrated ${allQuestions.length} questions.`);

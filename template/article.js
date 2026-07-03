function parseFrontmatter(markdown) {
    const frontmatterRegex = /^---\r?\n([\s\S]*?)\r?\n---/;
    const match = markdown.match(frontmatterRegex);

    if (!match) return { data: {}, content: markdown };

    const rawYaml = match[1];
    const content = markdown.replace(frontmatterRegex, '');
    const data = {};

    rawYaml.split('\n').forEach(line => {
        const parts = line.split(':');
        if (parts.length >= 2) {
            const key = parts[0].trim();
            let value = parts.slice(1).join(':').trim();

            if (value.startsWith('[') && value.endsWith(']')) {
                value = value.slice(1, -1).split(',').map(t => t.trim());
            }
            data[key] = value;
        }
    });

    return { data, content };
}

function renderArticleHeader(meta) {
    if (!meta.title) return '';

    let tagsHTML = '';
    if (Array.isArray(meta.tags)) {
        tagsHTML = `<div class="article-tags">` +
            meta.tags.map(tag => `<span class="article-tag">#${tag}</span>`).join('') +
            `</div>`;
    }

    return `
        <div class="article-header">
            <h1 class="article-title">${meta.title}</h1>
            <div class="article-meta">
                ${meta.author ? `<span>By <strong>${meta.author}</strong></span>` : ''}
                ${meta.date ? `<span>// Published: ${meta.date}</span>` : ''}
            </div>
            ${tagsHTML}
        </div>
    `;
}

const markdownRaw = document.getElementById("markdown-source").textContent.trim();

const { data, content } = parseFrontmatter(markdownRaw);

const headerHTML = renderArticleHeader(data);
const bodyHTML = marked.parse(content);

document.getElementById("content").innerHTML = headerHTML + bodyHTML;

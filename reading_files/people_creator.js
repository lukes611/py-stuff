const fs = require('fs');

const names = fs.readFileSync('./names.txt').toString().split('\n');

const subjects = 'math,science,art,law,engineering,business,dance,acting'.split(',');
const randomSubjects = (amount) => {
    const s = new Set();
    for(let i = 0; i < amount; i++) {
        const index = Math.floor(Math.random() * subjects.length);
        const subject = subjects[index];
        s.add(subject);
    }
    return [...s];
};

const ppl = names.map(name => {
    
    return {
        name,
        age: Math.floor(Math.random() * 40) + 18,
        phoneNumber: (() => {
            const x = (Math.random() * Math.pow(10, 14)).toString();
            let y = x.split('');
            y[4] = ' ';
            y[9] = ' ';
            return y.join('').slice(0, 13);
        })(),
        subjects: randomSubjects(Math.floor(Math.random() * 2 + 2)),

    };
});

fs.writeFileSync('people.json', JSON.stringify(ppl, null, 2));
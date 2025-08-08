const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'people.json');

// Create an empty JSON file if it doesn't exist
if (!fs.existsSync(filePath)) {
  fs.writeFileSync(filePath, JSON.stringify([]), 'utf-8');
}

// Read and return all people from the file
function getAllPeople() {
  const data = fs.readFileSync(filePath, 'utf-8');
  return JSON.parse(data);
}

// Save the updated list of people to the file
function savePeople(people) {
  fs.writeFileSync(filePath, JSON.stringify(people, null, 2), 'utf-8');
}

// Add a new person
function addPerson(name, age) {
  const people = getAllPeople();
  const newId = people.length > 0 ? people[people.length - 1].id + 1 : 1;
  const newPerson = { id: newId, name, age };
  people.push(newPerson);
  savePeople(people);
  console.log(`✅ ${name} was added with id=${newId}`);
}

// Search people by name (partial match)
function searchByName(query) {
  const people = getAllPeople();
  const results = people.filter(p => p.name.toLowerCase().includes(query.toLowerCase()));
  if (results.length === 0) {
    console.log('❌ No person found with that name.');
  } else {
    console.log('🔍 Search results by name:');
    console.table(results);
  }
}

// Search a person by exact ID
function searchById(id) {
  const people = getAllPeople();
  const result = people.find(p => p.id === id);
  if (!result) {
    console.log(`❌ No person found with id=${id}`);
  } else {
    console.log('🔍 Search result by ID:');
    console.table([result]);
  }
}

// -------------------------
// Example usage:

// Uncomment these to add people
// addPerson('mehdi', 17);
// addPerson('faeze', 30);
// addPerson('Reza', 28);
// addPerson('pooria', 23);
// addPerson('kiarash', 24);

// Example search
searchByName('k');
searchById(2);

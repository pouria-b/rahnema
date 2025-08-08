class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.length = 0;
  }

  // Add element to the start 
  prepend(value) {
    const newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
  }

  // Add element to the 
  append(value) {
    const newNode = new Node(value);
    if (!this.head) {
      this.head = newNode;
    } else {
      let curr = this.head;
      while (curr.next) {
        curr = curr.next;
      }
      curr.next = newNode;
    }
    this.length++;
  }

  // Return number of elements
  size() {
    return this.length;
  }

  // Return the value at index 
  at(index) {
    if (index < 0 || index > this.length) return undefined;
    let curr = this.head;
    let count = 0;
    while (curr && count < index) {
      curr = curr.next;
      count++;
    }
    return curr ? curr.value : undefined;
  }

  // Join another LinkedList 
  join(otherList) {
    let curr = otherList.head;
    while (curr) {
      this.append(curr.value);
      curr = curr.next;
    }
  }

  // Apply a function to all 
  map(fn) {
    let curr = this.head;
    while (curr) {
      curr.value = fn(curr.value);
      curr = curr.next;
    }
  }

  // Filter values 
  filter(predicate) {
    const filteredList = new LinkedList();
    let curr = this.head;
    while (curr) {
      if (predicate(curr.value)) {
        filteredList.append(curr.value);
      }
      curr = curr.next;
    }
    return filteredList;
  }


  print() {
    let curr = this.head;
    const values = [];
    while (curr) {
      values.push(curr.value);
      curr = curr.next;
    }
    console.log(values.join(" -> "));
  }
}





// test
// const list1 = new LinkedList();
// list1.append(7);
// list1.append(3);
// list1.append(9);
// list1.prepend(0);
// list1.print(); 
// console.log(list1.size()); 
// console.log(list1.at(2));  

// const list2 = new LinkedList();
// list2.append(6);
// list2.append(5);

// list1.join(list2);
// list1.print(); 

// list1.map(x => x * 2);
// list1.print(); 

// const filtered = list1.filter(x => x > 4);
// filtered.print(); 

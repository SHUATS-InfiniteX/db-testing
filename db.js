const mongoose = require('mongoose');

db_url = 'mongodb+srv://user_writer:yelH7iMCdK48hz6m@cluster1.hvtponu.mongodb.net/?retryWrites=true&w=majority'

mongoose.connect(db_url, { 
    useNewUrlParser: true, 
    useUnifiedTopology: true,
    dbName: 'user_db' });


const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
  console.log('Database connected successfully');
});

const Schema = mongoose.Schema;

const userSchema = new Schema({
    name: String,
    email: String,
    password: String
  },
  { collection: 'myCustomCollectionName', timestamps: true, versionKey: false});

const User = mongoose.model('User', userSchema);

const user = new User({ name: 'Johnny Sins', email: 'john@example.com', password: '123456' });

user.save()
  .then(doc => {
    console.log('User saved successfully', doc);
  })
  .catch(err => {
    console.error('Error saving user', err);
  });
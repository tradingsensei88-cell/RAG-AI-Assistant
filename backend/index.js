import express from 'express';
import cors from 'cors'
import 'dotenv/config'
import cookieParser from 'cookie-parser';
import connectMongoDB from './src/config/mongodb.js';
import chatRoutes from "./src/routes/chat.routes.js";

const app = express();

//CORS allow frontend to talk to backend
app.use(cors({
    origin: "http://localhost:5173", // ✅ allow frontend
    credentials: true,               // ✅ allow cookies
}));


// Parse incoming JSON requests (with large payload support)
app.use(express.json({ limit: '30mb' }));
app.use(express.urlencoded({ limit: '30mb', extended: true }));
app.use(cookieParser());

app.use("/api", chatRoutes);


app.get('/', (req, res) => {
    res.send("api is working")

})

const PORT = process.env.PORT || 3000;

async function startServer() {
    try {
        await connectMongoDB();
        app.listen(PORT, () => {
            console.log(`🚀 Server running on http://localhost:${PORT}`);
            console.log(`🚀 Ai running on http://localhost:8000/docs`);
        });
    } catch (error) {
        console.error('❌ Failed to start server:', error.message);
        process.exit(1);
    }
}

startServer();


export interface ServiceResponse {
    debugInfo: string;
    predictions: Prediction[];   
}

export interface Prediction{
    name: string;
    percentage: number;
    priority: number;
}

export interface DomainErrorProps {
	message: string;
	additionalData?: any;
	statusCode?: number;
}

export class DomainError extends Error {
	additionalData: any;
	statusCode: number;

	constructor({ message, additionalData }: DomainErrorProps) {
		super(message);
		this.additionalData = additionalData;
	}
}

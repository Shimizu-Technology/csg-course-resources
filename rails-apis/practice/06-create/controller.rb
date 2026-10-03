module Api
  module V1
    class WorkshopsController < ApplicationController
      before_action :set_session, only: %i[show update destroy]
      def index
        sessions = Workshop.order(:starts_on, :id)
        render json: sessions.map { |session| payload(session) }
      end

      def show
        render json: payload(@session)
      end
      def create
        session = Workshop.new(session_params)
        if session.save
          render json: payload(session), status: :created
        else
          render json: { errors: session.errors.full_messages }, status: :unprocessable_content
        end
      end
      def update
        head :not_implemented
      end
      def destroy
        head :not_implemented
      end
      private
      def session_params
        params.require(:workshop).permit(:title, :capacity, :starts_on)
      end
      def set_session
        @session = Workshop.find_by(id: params[:id])
        render json: { error: "workshop not found" }, status: :not_found unless @session
      end

      def payload(session)
        { id: session.id, title: session.title, capacity: session.capacity, starts_on: session.starts_on.iso8601 }
      end
    end
  end
end

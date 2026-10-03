module Api
  module V1
    class WorkshopsController < ApplicationController
      def index
        render json: []
      end
      def show
        head :not_implemented
      end
      def create
        head :not_implemented
      end
      def update
        head :not_implemented
      end
      def destroy
        head :not_implemented
      end
    end
  end
end
